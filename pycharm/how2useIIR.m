d1 = audioread("../data/Juliyalong.wav");
d1=d1(1e4:2:9e6,1);
decadeConstant=0.001;
f1=[];
ad1=abs(d1);
for j=2:length(d1)
    ad1(j)=ad1(j-1)+ad1(j);
    ad1(j)=ad1(j)*(1-decadeConstant);
end

filtered= filter(Bs(1,:),As(1,:),d1);
y=d1;
for n = 3:length(d1)
    y(n) = Bs(1,1) * d1(n) + Bs(1,2) * d1(n-1) + Bs(1,3) * d1(n-2) - As(1,2) * y(n-1) - As(1,3) * y(n-2);
end
%%
figure,hold on

plot(filtered(1:1000),'.')
plot(y(1:1000))
plot(d1(1:10),'x')
plot(sci,'o')

