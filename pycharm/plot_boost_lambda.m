% plot boost
figure
% semilogx(bo(:,1),bo(:,2),'yx')
semilogx(bo(:,1),bo(:,3),'o','color',[0.5, 0.9, 0.5]), hold on
testLambda=mean(reshape(bo(:,1), 3,[]));
testAccuracy=median(reshape(bo(:,3), 3,[]));
testAccuracyStd=std(reshape(bo(:,3), 3,[]));
testMean=mean(bo(:,3));
errorbar(testLambda,testAccuracy,testAccuracyStd,'k')
xlabel("Lambda")
ylabel("Test Accuracy")
