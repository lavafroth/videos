488d79fd       lea rdi, [rcx - 3]
4839f7         cmp rdi, rsi
0f8319010000   jae 0x8a06
488d79fe       lea rdi, [rcx - 2]
4839f7         cmp rdi, rsi
0f8315010000   jae 0x8a0f
488d79ff       lea rdi, [rcx - 1]
4839f7         cmp rdi, rsi
0f8311010000   jae 0x8a18
4839f1         cmp rcx, rsi
0f8311010000   jae 0x8a21
f30f1058c4     movss xmm3, dword [rax - 0x3c]
f30f5958cc     mulss xmm3, dword [rax - 0x34]
f30f5958d0     mulss xmm3, dword [rax - 0x30]
f30f58cb       addss xmm1, xmm3
f30f1058d4     movss xmm3, dword [rax - 0x2c]
f30f5958dc     mulss xmm3, dword [rax - 0x24]
f30f5958e0     mulss xmm3, dword [rax - 0x20]
f30f58d3       addss xmm2, xmm3
f30f1058e4     movss xmm3, dword [rax - 0x1c]
f30f1060ec     movss xmm4, dword [rax - 0x14]
f30f1068f0     movss xmm5, dword [rax - 0x10]
f30f1070f4     movss xmm6, dword [rax - 0xc]
0f14e6         unpcklps xmm4, xmm6
f30f1070fc     movss xmm6, dword [rax - 4]
0f14de         unpcklps xmm3, xmm6
0f59dc         mulps xmm3, xmm4
f30f1020       movss xmm4, dword [rax]
0f14ec         unpcklps xmm5, xmm4
0f59eb         mulps xmm5, xmm3
0f58c5         addps xmm0, xmm5
4883c104       add rcx, 4
4883c040       add rax, 0x40               ; elf_phdr
4881f90328..   cmp rcx, 0x2803
0f8566ffffff   jne 0x88e0
