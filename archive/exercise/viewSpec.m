[S,F,T,P] = spectrogram(data2(:,2),2048,1500,[],16000);
h = imagesc(T,F,10*log10(P));
xlabel('Time (secs)')
ylabel('Frequency (Hz)')
colorbar;
set(gca,'YDir','normal')
