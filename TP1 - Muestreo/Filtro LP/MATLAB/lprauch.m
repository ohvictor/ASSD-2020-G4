clear all
clc

f0 = 51054.08;
w0 = 2*pi*f0;
Q0 = 6.04;

R = 1.1e3;
C = 100e-12;

[R1,R2,R3,C1,C2] = part(w0,Q0,R,C);

R2 = 2.05e3;
C1 = 43e-9;

w0 = sqrt(1/(R2*R3*C1*C2));
Q0 = w0 * C1 / ( 1/R1 + 1/R2 + 1/R3 );

H = tf([w0^2],[1 w0/Q0 w0^2]);

f0 = w0/(2*pi)
Q0
R2
C1

bode(H);
grid on;
