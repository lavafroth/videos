│ │ ╎   │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87be(x)
│ │ ╎   │   0x00008870      483b742408     cmp rsi, qword [var_8h]
│ │ ╎  ┌──< 0x00008875      750d           jne 0x8884
│ │ ╎  ││   0x00008877      4889df         mov rdi, rbx                ; int64_t arg1
│ │ ╎  ││   0x0000887a      e891fdffff     call sym alloc::raw_vec::RawVec<T,A>
                                            ::grow_one::h4343ba1c9b16889b
                                            ; sym.alloc::raw_vec::RawVec_T_A_::grow_one::h4343ba1c9b16889b
│ │ ╎  ││                                   ; alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b
│ │ ╎  ││   0x0000887f      488b742418     mov rsi, qword [var_18h]
│ │ ╎  ││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8875(x)
│ │ ╎  └──> 0x00008884      f30f10542404   movss xmm2, dword [var_4h]
│ │ ╎   │   0x0000888a      0f28c2         movaps xmm0, xmm2
│ │ ╎   │   0x0000888d      f30f58c2       addss xmm0, xmm2
│ │ ╎   │   0x00008891      488b442410     mov rax, qword [var_10h]
│ │ ╎   │   0x00008896      4889f2         mov rdx, rsi
│ │ ╎   │   0x00008899      48c1e204       shl rdx, 4
│ │ ╎   │   0x0000889d      488d0c10       lea rcx, [rax + rdx]
│ │ ╎   │   0x000088a1      c704100000..   mov dword [rax + rdx], 0x3f800000 ; [0x3f800000:4]=-1
│ │ ╎   │   0x000088a8      f30f100d58..   movss xmm1, dword [0x00049008] ; [0x49008:4]=0x3e4ccccd
│ │ └─────< 0x000088b0      e997feffff     jmp 0x874c
│ │     │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x876d(x)
│ └───────> 0x000088b5      488b5c2408     mov rbx, qword [var_8h]
│       │   0x000088ba      4c8b742410     mov r14, qword [var_10h]
│       │   0x000088bf      498d463c       lea rax, [r14 + 0x3c]
│       │   0x000088c3      0f57c0         xorps xmm0, xmm0
│       │   0x000088c6      0f57c9         xorps xmm1, xmm1
│       │   0x000088c9      b903000000     mov ecx, 3
│       │   0x000088ce      488d15a305..   lea rdx, [0x00058e78]
│       │   0x000088d5      0f57d2         xorps xmm2, xmm2
│       │   0x000088d8      0f1f840000..   nop dword [rax + rax]
│       │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8974(x)
│      ┌──> 0x000088e0      488d79fd       lea rdi, [rcx - 3]
│      ╎│   0x000088e4      4839f7         cmp rdi, rsi
│     ┌───< 0x000088e7      0f8319010000   jae 0x8a06
│     │╎│   0x000088ed      488d79fe       lea rdi, [rcx - 2]
│     │╎│   0x000088f1      4839f7         cmp rdi, rsi
│    ┌────< 0x000088f4      0f8315010000   jae 0x8a0f
│    ││╎│   0x000088fa      488d79ff       lea rdi, [rcx - 1]
│    ││╎│   0x000088fe      4839f7         cmp rdi, rsi
│   ┌─────< 0x00008901      0f8311010000   jae 0x8a18
│   │││╎│   0x00008907      4839f1         cmp rcx, rsi
│  ┌──────< 0x0000890a      0f8311010000   jae 0x8a21
│  ││││╎│   0x00008910      f30f1058c4     movss xmm3, dword [rax - 0x3c]
│  ││││╎│   0x00008915      f30f5958cc     mulss xmm3, dword [rax - 0x34]
│  ││││╎│   0x0000891a      f30f5958d0     mulss xmm3, dword [rax - 0x30]
│  ││││╎│   0x0000891f      f30f58cb       addss xmm1, xmm3
│  ││││╎│   0x00008923      f30f1058d4     movss xmm3, dword [rax - 0x2c]
│  ││││╎│   0x00008928      f30f5958dc     mulss xmm3, dword [rax - 0x24]
│  ││││╎│   0x0000892d      f30f5958e0     mulss xmm3, dword [rax - 0x20]
│  ││││╎│   0x00008932      f30f58d3       addss xmm2, xmm3
│  ││││╎│   0x00008936      f30f1058e4     movss xmm3, dword [rax - 0x1c]
│  ││││╎│   0x0000893b      f30f1060ec     movss xmm4, dword [rax - 0x14]
│  ││││╎│   0x00008940      f30f1068f0     movss xmm5, dword [rax - 0x10]
│  ││││╎│   0x00008945      f30f1070f4     movss xmm6, dword [rax - 0xc]
│  ││││╎│   0x0000894a      0f14e6         unpcklps xmm4, xmm6
│  ││││╎│   0x0000894d      f30f1070fc     movss xmm6, dword [rax - 4]
│  ││││╎│   0x00008952      0f14de         unpcklps xmm3, xmm6
│  ││││╎│   0x00008955      0f59dc         mulps xmm3, xmm4
│  ││││╎│   0x00008958      f30f1020       movss xmm4, dword [rax]
│  ││││╎│   0x0000895c      0f14ec         unpcklps xmm5, xmm4
│  ││││╎│   0x0000895f      0f59eb         mulps xmm5, xmm3
│  ││││╎│   0x00008962      0f58c5         addps xmm0, xmm5
│  ││││╎│   0x00008965      4883c104       add rcx, 4
│  ││││╎│   0x00008969      4883c040       add rax, 0x40               ; elf_phdr
│  ││││╎│   0x0000896d      4881f90328..   cmp rcx, 0x2803
│  ││││└──< 0x00008974      0f8566ffffff   jne 0x88e0
│  ││││ │   0x0000897a      f30f58ca       addss xmm1, xmm2
│  ││││ │   0x0000897e      f30f58c8       addss xmm1, xmm0
