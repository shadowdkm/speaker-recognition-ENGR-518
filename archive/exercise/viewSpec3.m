clear all
load matlab.mat

subplot(3,1,1)
[S,F,TJuliya,PJuliya] = spectrogram(Juliya,2048,2000,[],16000);
h = imagesc(TJuliya,F,10*log10(PJuliya));
ylabel('Juliya Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])

subplot(3,1,2)
[S,F,TShubham,PShubham] = spectrogram(Shubham,2048,2000,[],16000);
h = imagesc(TShubham,F,10*log10(PShubham));
ylabel('Shubham Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])

subplot(3,1,3)
[S,F,TShadow,PShadow] = spectrogram(Shadow,2048,2000,[],16000);
h = imagesc(TShadow,F,10*log10(PShadow));
xlabel('Time (secs)')
ylabel('Shadow Frequency (Hz)')
set(gca,'YDir','normal')
ylim([0,3000])

%% All data used
dataset=[log10(PJuliya),log10(PShubham),log10(PShadow)];
labels=[TJuliya*0+1,TShubham*0+0,TShadow*0+0;
        TJuliya*0+0,TShubham*0+1,TShadow*0+0;
        TJuliya*0+0,TShubham*0+0,TShadow*0+1];

%% Data Larger than threshold
VJuliya=PJuliya(:,max(log10(PJuliya),[],1)>-5);
VShubham=PShubham(:,max(log10(PShubham),[],1)>-5);
VShadow=PShadow(:,max(log10(PShadow),[],1)>-5);
vdataset=[VJuliya,VShubham,VShadow];

vlabels=[VJuliya(1,:)*0+1,VShubham(1,:)*0+0,VShadow(1,:)*0+0;
         VJuliya(1,:)*0+0,VShubham(1,:)*0+1,VShadow(1,:)*0+0;
         VJuliya(1,:)*0+0,VShubham(1,:)*0+0,VShadow(1,:)*0+1];

