function [x,n] = stepseq(a,b,c)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
x=zeros(1,c);
n=a:c;

for i=b:length(n)
    x(i)=1;
end

end

