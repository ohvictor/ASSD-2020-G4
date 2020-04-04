function [R1,R2,R3,C1,C2] = part(w0,Q0,R,C)
%[R1,R2,R3,C1,C2] = part(w0,Q0,R,C)
ka = 1/w0/R/C;
a2 = 0.5*(ka/Q0-1);
k2 = ka^2/a2;

R1 = R;
R2 = a2*R;
R3 = R;

C1 = k2*C;
C2 = C;
end

