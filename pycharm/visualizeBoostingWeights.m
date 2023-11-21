w1s=[];
w2s=[];
w3s=[];
F=50:10:1000;
for i=2:28
    weights = readmatrix(sprintf("boost_%d.csv",i));
    w1s=[w1s; weights(1,2:end)];
    w2s=[w2s; weights(2,2:end)];
    w3s=[w3s; weights(3,2:end)];
end

%%
lambda=[1048576,524288,262144,131072,65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32,16,8,4,2,1,0.5,0.25,0.125,0.0625,0.03125,0.015625];

figure(1)
subplot1=subplot(3,1,1);
surf(F,lambda,w1s,'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #1"})
subplot2=subplot(3,1,2);
surf(F,lambda,w2s,'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #2"})
subplot3=subplot(3,1,3);
surf(F,lambda,w3s,'LineStyle','none'), xlim([0,1000]),ylabel({"Lambda","Subject #3"})
xlabel("Frequency")

view(subplot1,[0.0375000000000014 90]);grid(subplot1,'on');hold(subplot1,'off');set(subplot1,'YMinorTick','on','YScale','log');
view(subplot2,[0.0375000000000014 90]);grid(subplot2,'on');hold(subplot2,'off');set(subplot2,'YMinorTick','on','YScale','log');
view(subplot3,[0.0375000000000014 90]);grid(subplot3,'on');hold(subplot3,'off');set(subplot3,'YMinorTick','on','YScale','log');