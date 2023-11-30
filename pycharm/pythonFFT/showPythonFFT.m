sub1=readmatrix("subject1.csv");
sub2=readmatrix("subject2.csv");
sub3=readmatrix("subject3.csv");


F=linspace(0,8000,1025);


%%
figure(2)
subplot(3,1,1)
plot(F(1:150),sub1(1:3:end,:),'Color',[0.9 0.2 0.5 0.02])
ylabel(["Subject 1", "Power (dB)"])
xlim([0,1000])

subplot(3,1,2)
plot(F(1:150),sub2(1:3:end,:),'Color',[0.9 0.5 0.2 0.02])
ylabel(["Subject 2","Power (dB)"])
xlim([0,1000])
subplot(3,1,3)
plot(F(1:150),sub3(1:3:end,:),'Color',[0.2 0.5 0.9 0.02])
ylabel(["Subject 3","Power (dB)"])
xlim([0,1000])
xlabel("Frequency (Hz)")