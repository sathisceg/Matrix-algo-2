
A = sprand(1000,1000,0.005);
A = A'; 
q0 = rand(1000,1);
q0 = sparse(q0); 
m = 50;  

for i = 1:m
    q1 = A*q0;
    q1 = q1/norm(q1);
    if norm(q1 - q0,1) < 14^(-10)
        norm(q1 - q0,1)
        q1
        break;
    end
    q0 = q1;
end


    