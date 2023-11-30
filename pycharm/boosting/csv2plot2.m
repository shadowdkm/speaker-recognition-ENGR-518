
w0=zeros(22,151);
w1=zeros(22,151);
w2=zeros(22,151);

for i=1:22
    for j=0:2        
        filename=sprintf("boost_%03d_%03d.csv",i+2,j);
        disp(filename)
        boost3 = readmatrix(filename);
        w0(i,:)=w0(i,:)+boost3(1,:);
        w1(i,:)=w1(i,:)+boost3(2,:);
        w2(i,:)=w2(i,:)+boost3(3,:);
    end
end
%%
F=linspace(0,8000,1025);
F=F(2:151);
lambda=2.^(22:-1:1);
figure(1)
subplot1=subplot(3,1,1);
surf(F,lambda,w0(:,2:end),'LineStyle','none'), xlim([0,60]),ylabel({"Lambda","Subject #1"})
subplot2=subplot(3,1,2);
surf(F,lambda,w1(:,2:end),'LineStyle','none'), xlim([0,60]),ylabel({"Lambda","Subject #2"})
subplot3=subplot(3,1,3);
surf(F,lambda,w2(:,2:end),'LineStyle','none'), xlim([0,60]),ylabel({"Lambda","Subject #3"})
xlabel("Frequency")


view(subplot1,[0.0 90]);grid(subplot1,'on');hold(subplot1,'off');set(subplot1,'YMinorTick','on','YScale','log');
view(subplot2,[0.0 90]);grid(subplot2,'on');hold(subplot2,'off');set(subplot2,'YMinorTick','on','YScale','log');
view(subplot3,[0.0 90]);grid(subplot3,'on');hold(subplot3,'off');set(subplot3,'YMinorTick','on','YScale','log');

%%
figure(8)
subplot(2,1,1)
plot(F(1:150),sub1(1:3:end,:),'Color',[0.9 0.2 0.5 0.02])
ylabel(["Subject 1", "Power (dB)"])
xlim([0,1000])

subplot1=subplot(2,1,2);
surf(F,lambda,w0(:,2:end),'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #1"})
view(subplot1,[0.0 90]);grid(subplot1,'on');hold(subplot1,'off');set(subplot1,'YMinorTick','on','YScale','log');
xlabel("Frequency (Hz)")