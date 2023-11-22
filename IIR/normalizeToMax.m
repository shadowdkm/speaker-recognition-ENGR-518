function f1n=normalizeToMax(x)
    f1n=x';
    f1mean=mean(f1n);
    f1n=f1n-f1mean;
    f1range=max(f1n)-min(f1n);
    f1n = bsxfun(@rdivide,f1n, f1range);
end