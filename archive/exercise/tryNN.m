[S,F,T,Pshadowlong] = spectrogram(shadowlong(:,1),2048,2000,[],16000);
h = imagesc(T,F,10*log10(Pshadowlong));
xlabel('Time (secs)')
ylabel('Shadow Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])
%%
VShadowlong=Pshadowlong(:,max(log10(Pshadowlong),[],1)>-5);
Yc = NN3.Network(log10(VShadowlong));
plot(Yc')