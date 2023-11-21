pkg load signal

sf=8000;
sf2=sf/2;

bs=[];
as=[];

#boostedFrequency=[7.8,15.6,31.25,54,85,117,148,210,234,265,187,312,375,406]

for i=[50,100,150,240,340,420]
  [b,a]=pei_tseng_notch ( i / sf2, 20/sf2 );
  bs=[bs;b];
  as=[as;a];
end

dlmwrite ("bs8kboost.csv", bs, ",")
dlmwrite ("as8kboost.csv", as, ",")
