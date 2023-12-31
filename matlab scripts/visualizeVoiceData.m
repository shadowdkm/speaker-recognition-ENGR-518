clear all

d1 = audioread("../data/wav1.wav");
d1=gpuArray(d1(:,1));
[~,~,T1,P1] = spectrogram(d1,2048,512,[],16000);
V1=P1(1:150,:);
P1=[];d1=[];

d2 = audioread("../data/wav2.wav");
d2=gpuArray(d2(:,1));
[~,~,T2,P2] = spectrogram(d2,2048,512,[],16000);
V2=P2(1:150,:);
P2=[];d2=[];

d3 = audioread("../data/wav3.wav");
d3=gpuArray(d3(:,1));
[S,F,T3,P3] = spectrogram(d3,2048,512,[],16000);
V3=P3(1:150,:);
P3=[];d3=[];

%% All data used
dataset=[log10(V1),log10(V2),log10(V3)];
labels=[V1(1,:)*0+1,V2(1,:)*0+0,V3(1,:)*0+0;
        V1(1,:)*0+0,V2(1,:)*0+1,V3(1,:)*0+0;
        V1(1,:)*0+0,V2(1,:)*0+0,V3(1,:)*0+1];

%%
figure(2)
subplot(3,1,1)
plot(F(1:150),log10(V1(1:150,1:5:end)),'Color',[0.9 0.2 0.5 0.02])
ylabel(["Subject 1", "Power (dB)"])
ylim([-12,-3]),xlim([0,1000])

subplot(3,1,2)
plot(F(1:150),log10(V2(1:150,1:3:end)),'Color',[0.9 0.5 0.2 0.02])
ylabel(["Subject 2","Power (dB)"])
ylim([-12,-3]),xlim([0,1000])
subplot(3,1,3)
plot(F(1:150),log10(V3(1:150,1:3:end)),'Color',[0.2 0.5 0.9 0.02])
ylabel(["Subject 3","Power (dB)"])
ylim([-12,-3]),xlim([0,1000])
xlabel("Frequency (Hz)")

