close all
clear all

T=50;

a=1;
b=-.5;
xn1 = 0;
xn2=0;
yn1=0;
yn2=0;
y=[];

[x,n]=impseq(1,1,T);

for i=1:length(n)
    y(i)=0.5*xn2+a*yn1+b*yn2;
    xn2=xn1;
    xn1=x(i);
    yn2=yn1;
    yn1=y(i);
end

subplot(3,2,1)
stem(y);
xlabel('x(n)=delta -> h(n) simulado')
grid on
title('alpha=1; beta=-0.5')

[x,n]=stepseq(1,1,T);

for i=1:length(n)
    y(i)=0.5*xn2+a*yn1+b*yn2;
    xn2=xn1;
    xn1=x(i);
    yn2=yn1;
    yn1=y(i);
end

subplot(3,2,2)
stem(y);
xlabel('x(n)=delta -> h(n) simulado')
grid on
title('alpha=1; beta=-0.5')

a=0.5;
b=-.125;
xn1 = 0;
xn2=0;
yn1=0;
yn2=0;
y=[];

[x,n]=impseq(1,1,T);

for i=1:length(n)
    y(i)=0.5*xn2+a*yn1+b*yn2;
    xn2=xn1;
    xn1=x(i);
    yn2=yn1;
    yn1=y(i);
end

subplot(3,2,3)
stem(y);
xlabel('x(n)=delta -> h(n) simulado')
grid on
title('alpha=0.5; beta=-0.125')

[x,n]=stepseq(1,1,T);

for i=1:length(n)
    y(i)=0.5*xn2+a*yn1+b*yn2;
    xn2=xn1;
    xn1=x(i);
    yn2=yn1;
    yn1=y(i);
end

subplot(3,2,4)
stem(y);
xlabel('x(n)=delta -> h(n) simulado')
title('alpha=0.5; beta=-0.125')
grid on

a=5/4;
b=-25/32;
xn1 = 0;
xn2=0;
yn1=0;
yn2=0;
y=[];

[x,n]=impseq(1,1,T);

for i=1:length(n)
    y(i)=0.5*xn2+a*yn1+b*yn2;
    xn2=xn1;
    xn1=x(i);
    yn2=yn1;
    yn1=y(i);
end

subplot(3,2,5)
stem(y);
xlabel('x(n)=delta -> h(n) simulado')
title('alpha=5/4; beta=-25/32')

grid on

[x,n]=stepseq(1,1,T);

for i=1:length(n)
    y(i)=0.5*xn2+a*yn1+b*yn2;
    xn2=xn1;
    xn1=x(i);
    yn2=yn1;
    yn1=y(i);
end

subplot(3,2,6)
stem(y);
xlabel('x(n)=escalón -> h(n) simulado')
title('alpha=5/4; beta=-25/32')
grid on