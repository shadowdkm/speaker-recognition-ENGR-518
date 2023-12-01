clear all

fftpoints=2048*4;
fLength=200;
d01 = audioread("../data/wav1.wav");
d02 = audioread("../data/wav2.wav");
d03 = audioread("../data/wav3.wav");
d1=gpuArray(d01(:,1));
[~,~,T1,P1] = spectrogram(d01,fftpoints,fftpoints-512,[],16000);V1=P1(1:fLength,:);clear P1 d1
d2=gpuArray(d02(:,1));
[~,~,T2,P2] = spectrogram(d02,fftpoints,fftpoints-512,[],16000);V2=P2(1:fLength,:);clear P2 d2
d3=gpuArray(d03(:,1));
[S,F,T3,P3] = spectrogram(d03,fftpoints,fftpoints-512,[],16000);V3=P3(1:fLength,:);clear P3 d3

%%
alpha=0.01;
downsample=6;
figure(2)
clf, hold on
plot(F(1:fLength),log10(V1(1:fLength,1:downsample:end)),'Color',[0.9 0.2 0.5 alpha])
plot(F(1:fLength),log10(V2(1:fLength,1:downsample:end)),'Color',[0.9 0.5 0.2 alpha])
plot(F(1:fLength),log10(V3(1:fLength,1:downsample:end)),'Color',[0.2 0.5 0.9 alpha])
xlim([0,300])