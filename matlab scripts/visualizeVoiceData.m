clear all

d1 = audioread("../data/Juliyalong.wav");
d1=d1(:,1);
[~,~,T1,P1] = spectrogram(d1,2048,2000,[],16000);
V1=P1(1:260,max(log10(P1),[],1)>-5);
P1=[];d1=[];

d2 = audioread("../data/Shubhamlong.wav");
d2=d2(:,1);
[~,~,T2,P2] = spectrogram(d2,2048,2000,[],16000);
V2=P2(1:260,max(log10(P2),[],1)>-5);
P2=[];d2=[];

d3 = audioread("../data/Shadowlong.wav");
d3=d3(:,1);
[S,F,T3,P3] = spectrogram(d3,2048,2000,[],16000);
V3=P3(1:260,max(log10(P3),[],1)>-5);
P3=[];d3=[];

%% All data used
dataset=[log10(V1),log10(V2),log10(V3)];
labels=[V1(1,:)*0+1,V2(1,:)*0+0,V3(1,:)*0+0;
        V1(1,:)*0+0,V2(1,:)*0+1,V3(1,:)*0+0;
        V1(1,:)*0+0,V2(1,:)*0+0,V3(1,:)*0+1];

%%
figure(2)
subplot(3,1,1)
plot(F(1:150),log10(V1(1:150,1:100:end)),'Color',[0.9 0.2 0.5 0.02])
ylabel(["Subject 1", "Power (dB)"])

subplot(3,1,2)
plot(F(1:150),log10(V2(1:150,1:100:end)),'Color',[0.9 0.5 0.2 0.02])
ylabel(["Subject 2","Power (dB)"])

subplot(3,1,3)
plot(F(1:150),log10(V3(1:150,1:100:end)),'Color',[0.2 0.5 0.9 0.02])
ylabel(["Subject 3","Power (dB)"])

xlabel("Frequency (Hz)")

