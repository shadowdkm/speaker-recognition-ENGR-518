% plot boost
figure
% semilogx(bo(:,1),bo(:,2),'yx')
semilogx(bo(:,1),bo(:,3),'go'), hold on
testMean=mean(bo(:,3));
xlabel("Lambda")
ylabel("Test Accuracy")