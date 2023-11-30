%matlabANN

subs=[sub1(1:3000,:);sub2(1:3000,:);sub3(1:3000,:)];
labels=zeros(9000,3);
labels(1:3000,1)=1;
labels(1:3000+3000,2)=1;
labels(1:3000+6000,3)=1;
