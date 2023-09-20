clear all
load matlab.mat

subplot(3,1,1)
[S,F,T,P] = spectrogram(Juliya,2048,2000,[],16000);
h = imagesc(T,F,10*log10(P));
ylabel('Juliya Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])

subplot(3,1,2)
[S,F,T,P] = spectrogram(Shubham,2048,2000,[],16000);
h = imagesc(T,F,10*log10(P));
ylabel('Shubham Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])

subplot(3,1,3)
[S,F,T,P] = spectrogram(Shadow,2048,2000,[],16000);
h = imagesc(T,F,10*log10(P));
xlabel('Time (secs)')
ylabel('Shadow Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])