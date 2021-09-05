`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/26/2021 04:28:27 PM
// Design Name: 
// Module Name: Lab4
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module half_adder(
    input wire a,
    input wire b,
    output wire s,
    output wire c
    );
    
    xor xor1(s, a, b);
    and and1(c, a, b);
    
endmodule

module full_adder(
    input wire a,
    input wire b,
    input wire cin,
    output wire s,
    output wire cout
    );
    
    wire x1, a1, a2;
    half_adder half_adder1(a, b, x1, a1);
    half_adder half_adder2(x1, cin, s, a2);
    or or1(cout, a1, a2);

endmodule

module fourbit_addsub(
    input wire cin,
    input wire a0, a1, a2, a3,
    input wire b0, b1, b2, b3,
    output wire cout,
    output wire s0, s1, s2, s3
    );
    
    wire x0, x1, x2, x3;
    wire c1, c2, c3;
    xor xor1(x0, b0, cin);
    xor xor2(x1, b1, cin);
    xor xor3(x2, b2, cin);
    xor xor4(x3, b3, cin);
    
    full_adder full_adder1(a0, x0, cin, s0, c1);
    full_adder full_adder2(a1, x1, c1, s1, c2);
    full_adder full_adder3(a2, x2, c2, s2, c3);
    full_adder full_adder4(a3, x3, c3, s3, cout);
endmodule