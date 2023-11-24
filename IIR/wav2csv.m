clear all

d1 = audioread("../pycharm/Juliyav3.wav");
% d1=d1(1e4:2:9e6,1);

d2 = audioread("../pycharm/Shubhamv3.wav");
% d2=d2(1e4:2:9e6,1);

d3 = audioread("../pycharm/Shadowv3.wav");
% d3=d3(1e4:2:9e6,1);


As = readmatrix("as8k.csv");
Bs = readmatrix("bs8k.csv");

decadeConstant=0.001;
thresold=10;
%%
f1=[];
ad1= filter(decadeConstant,[1,decadeConstant-1],abs(d1))/decadeConstant;
for i=1:size(As,1)
   filtered= filter(Bs(i,:),As(i,:),d1);
   filtered=filtered-d1;
   filtered= filter(decadeConstant,[1,decadeConstant-1],abs(filtered));
   f1=[f1,filtered];
end
f2=[];
ad2= filter(decadeConstant,[1,decadeConstant-1],abs(d2))/decadeConstant;
for i=1:size(As,1)
   filtered= filter(Bs(i,:),As(i,:),d2);
   filtered=filtered-d2;
   filtered= filter(decadeConstant,[1,decadeConstant-1],abs(filtered));
   f2=[f2,filtered];
end

f3=[];
ad3= filter(decadeConstant,[1,decadeConstant-1],abs(d3))/decadeConstant;
for i=1:size(As,1)
   filtered= filter(Bs(i,:),As(i,:),d3);
   filtered=filtered-d3;
   filtered= filter(decadeConstant,[1,decadeConstant-1],abs(filtered));
   f3=[f3,filtered];
end
%% domastic normalization
% f3n = bsxfun(@rdivide, f3(1:1000:end,:), ad3(1:1000:end));
% f2n = bsxfun(@rdivide, f2(1:1000:end,:), ad2(1:1000:end));
% f1n = bsxfun(@rdivide, f1(1:1000:end,:), ad1(1:1000:end));
subsetI=[1,6,11,20,30,38];
epsilon=0.0001;
f1n=normalizeToMax(log10(f1(1:1000:end,:)));
f2n=normalizeToMax(log10(f2(1:1000:end,:)));
f3n=normalizeToMax(log10(f3(1:1000:end,:)));
f1ns=normalizeToMax(log10(f1(1:1000:end,subsetI)));
f2ns=normalizeToMax(log10(f2(1:1000:end,subsetI)));
f3ns=normalizeToMax(log10(f3(1:1000:end,subsetI)));


%%
f1=f1(ad1>thresold,:);
f2=f2(ad2>thresold,:);
f3=f3(ad3>thresold,:);

%%
f1=f1(1:1000:end,:);
f2=f2(1:1000:end,:);
f3=f3(1:1000:end,:);
%%
figure
subplot(3,1,1),imagesc(log10(f1)')
subplot(3,1,2),imagesc(log10(f2)')
subplot(3,1,3),imagesc(log10(f3)')
figure
subplot(3,1,1),plot(50:10:1000,log10(f1(1:end,:))','Color',[0.9 0.5 0.2 0.02])
subplot(3,1,2),plot(50:10:1000,log10(f2(1:end,:))','Color',[0.2 0.9 0.5 0.02])
subplot(3,1,3),plot(50:10:1000,log10(f3(1:end,:))','Color',[0.2 0.5 0.9 0.02])

csvwrite("iir1.csv",log10(f1)');
csvwrite("iir2.csv",log10(f2)');
csvwrite("iir3.csv",log10(f3)');
%% subset of boosting results
F=50:10:1000;
subsetF=[50,100,150,240,340,420]';

subsetI=[1,6,11,20,30,38];

csvwrite("iir1_subset.csv",log10(f1(:,subsetI))');
csvwrite("iir2_subset.csv",log10(f2(:,subsetI))');
csvwrite("iir3_subset.csv",log10(f3(:,subsetI))');

%%
csvwrite("iir1_selfNorm.csv",(f1n));
csvwrite("iir2_selfNorm.csv",(f2n));
csvwrite("iir3_selfNorm.csv",(f3n));
csvwrite("iir1_selfNorm_subset.csv",log10(f1(:,subsetI)));
csvwrite("iir2_selfNorm_subset.csv",log10(f2(:,subsetI)));
csvwrite("iir3_selfNorm_subset.csv",log10(f3(:,subsetI)));