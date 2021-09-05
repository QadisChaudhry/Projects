`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/26/2021 05:04:56 PM
// Design Name: 
// Module Name: fourbit_addsub_sim
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


module fourbit_addsub_sim();

reg cin;
reg a0, a1, a2, a3;
reg b0, b1, b2, b3;
wire cout;
wire s0, s1, s2, s3;

fourbit_addsub simulation(cin, a0, a1, a2, a3, b0, b1, b2, b3, cout, s0, s1, s2, s3);

initial
begin

cin = 0;
a0 = 0;
a1 = 0;
a2 = 0; 
a3 = 0;
b0 = 0;
b1 = 0;
b2 = 0; 
b3 = 0;

#10;

#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00000001;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00000010;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00000100;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00001000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00010000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00100000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b01000000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b10000000;
#5 {cin} = 1'b1;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00000001;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00000010;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00000100;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00001000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00010000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b00100000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b01000000;
#5 {a0, a1, a2, a3, b0, b1, b2, b3} = 8'b10000000;

#5;
$finish;

end

endmodule
