%Filter Cell component Calculator

clear all
clc

f = [51054.08; 44372.79; 33682.41; 24398.21];
Q = [6.04; 1.84; 0.91; 0.54];

w = f*2*pi;

R=1e3;
C=100e-12;

Cell = zeros(4,5);

for i=1:length(f)
    [R1,R2,R3,C1,C2] = part(w(i),Q(i),R,C);
    a = [R1 R2 R3 C1 C2]
    Cell(i,:)= a
end
