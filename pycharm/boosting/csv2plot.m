

l=dir("*.csv");

w0=zeros(length(l),151);
w1=zeros(length(l),151);
w2=zeros(length(l),151);
F=linspace(0,8000,1025);
F=F(1:151);
lambda=[testLambda,8];
for i=1:length(l)
    boost3 = readmatrix(l(i).name);
    w0(i,:)=boost3(1,:);
    w1(i,:)=boost3(2,:);
    w2(i,:)=boost3(3,:);
end

figure(1)
subplot1=subplot(3,1,1);
surf(F,lambda,w0,'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #1"})
subplot2=subplot(3,1,2);
surf(F,lambda,w1,'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #2"})
subplot3=subplot(3,1,3);
surf(F,lambda,w2,'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #3"})
xlabel("Frequency")


view(subplot1,[0.0 90]);grid(subplot1,'on');hold(subplot1,'off');set(subplot1,'YMinorTick','on','YScale','log');
view(subplot2,[0.0 90]);grid(subplot2,'on');hold(subplot2,'off');set(subplot2,'YMinorTick','on','YScale','log');
view(subplot3,[0.0 90]);grid(subplot3,'on');hold(subplot3,'off');set(subplot3,'YMinorTick','on','YScale','log');