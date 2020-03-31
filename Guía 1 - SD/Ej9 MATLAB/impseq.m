function [x,n] = impseq(a,b,c)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

x=zeros(1,c);
n=a:c;

x(b)=1;
end

