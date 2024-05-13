            ; DATA XREF from main @ 0x8a87(r)
┌ 884: sym.cleancode::main::he34f242c79130c17 ();
│           ; var int64_t var_4h @ rsp-0xac
│           ; var uint32_t var_8h @ rsp-0xa8
│           ; var uint32_t var_10h @ rsp-0xa0
│           ; var int64_t var_18h @ rsp-0x98
│           ; var int64_t var_20h @ rsp-0x90
│           ; var int64_t var_28h @ rsp-0x88
│           ; var int64_t var_3ch @ rsp-0x74
│           ; var int64_t var_40h @ rsp-0x70
│           ; var int64_t var_48h @ rsp-0x68
│           0x000086c0      4157           push r15                    ; cleancode::main::he34f242c79130c17
│           0x000086c2      4156           push r14
│           0x000086c4      53             push rbx
│           0x000086c5      4883ec50       sub rsp, 0x50
│           0x000086c9      488d059239..   lea rax, obj.__rust_no_alloc_shim_is_unstable ; 0x5c062
│           0x000086d0      0fb600         movzx eax, byte [rax]
│           0x000086d3      bf00800200     mov edi, 0x28000
│           0x000086d8      be04000000     mov esi, 4
│           0x000086dd      ff155d340500   call qword [sym.__rust_alloc] ; [0x5bb40:8]=0x8ab0 sym.__rust_alloc
│           0x000086e3      4885c0         test rax, rax
│       ┌─< 0x000086e6      0f8440030000   je 0x8a2c
│       │   0x000086ec      48c7442408..   mov qword [var_8h], 0x2800  ; [0x2800:8]=8
│       │   0x000086f5      4889442410     mov qword [var_10h], rax
│       │   0x000086fa      48c7442418..   mov qword [var_18h], 0
│       │   0x00008703      31f6           xor esi, esi
│       │   0x00008705      4c8d35a009..   lea r14, [0x000490ac]
│       │   0x0000870c      488d5c2408     lea rbx, [var_8h]
│       │   0x00008711      4531ff         xor r15d, r15d
│      ┌──< 0x00008714      eb5d           jmp 0x8773
..
│      ││   ; CODE XREFS from cleancode::main::he34f242c79130c17 @ 0x8805(x), 0x8818(x)
│    ┌┌───> 0x00008720      f30f10542404   movss xmm2, dword [var_4h]
│    ╎╎││   0x00008726      0f28c2         movaps xmm0, xmm2
│    ╎╎││   0x00008729      f30f58c2       addss xmm0, xmm2
│    ╎╎││   0x0000872d      488b442410     mov rax, qword [var_10h]
│    ╎╎││   0x00008732      4889f2         mov rdx, rsi
│    ╎╎││   0x00008735      48c1e204       shl rdx, 4
│    ╎╎││   0x00008739      488d0c10       lea rcx, [rax + rdx]
│    ╎╎││   0x0000873d      c704100000..   mov dword [rax + rdx], 0x3f000000 ; [0x3f000000:4]=-1
│    ╎╎││   0x00008744      f30f100db8..   movss xmm1, dword [0x00049004] ; [0x49004:4]=0x3dcccccd
│    ╎╎││   ; CODE XREFS from cleancode::main::he34f242c79130c17 @ 0x885c(x), 0x88b0(x)
│  ┌┌─────> 0x0000874c      49ffc7         inc r15
│  ╎╎╎╎││   0x0000874f      f30f114904     movss dword [rcx + 4], xmm1
│  ╎╎╎╎││   0x00008754      f30f115108     movss dword [rcx + 8], xmm2
│  ╎╎╎╎││   0x00008759      f30f11410c     movss dword [rcx + 0xc], xmm0
│  ╎╎╎╎││   0x0000875e      48ffc6         inc rsi
│  ╎╎╎╎││   0x00008761      4889742418     mov qword [var_18h], rsi
│  ╎╎╎╎││   0x00008766      4981ff0028..   cmp r15, 0x2800
│ ┌───────< 0x0000876d      0f8442010000   je 0x88b5
│ │╎╎╎╎││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8714(x)
│ │╎╎╎╎└──> 0x00008773      4d85ff         test r15, r15
│ │╎╎╎╎┌──< 0x00008776      7818           js 0x8790
│ │╎╎╎╎││   0x00008778      0f57c0         xorps xmm0, xmm0
│ │╎╎╎╎││   0x0000877b      f3490f2ac7     cvtsi2ss xmm0, r15
│ ────────< 0x00008780      eb29           jmp 0x87ab
..
│ │╎╎╎╎││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8776(x)
│ │╎╎╎╎└──> 0x00008790      4c89f9         mov rcx, r15
│ │╎╎╎╎ │   0x00008793      48d1e9         shr rcx, 1
│ │╎╎╎╎ │   0x00008796      4489fa         mov edx, r15d
│ │╎╎╎╎ │   0x00008799      83e201         and edx, 1
│ │╎╎╎╎ │   0x0000879c      4809ca         or rdx, rcx
│ │╎╎╎╎ │   0x0000879f      0f57c0         xorps xmm0, xmm0
│ │╎╎╎╎ │   0x000087a2      f3480f2ac2     cvtsi2ss xmm0, rdx
│ │╎╎╎╎ │   0x000087a7      f30f58c0       addss xmm0, xmm0
│ │╎╎╎╎ │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8780(x)
│ ────────> 0x000087ab      f30f11442404   movss dword [var_4h], xmm0
│ │╎╎╎╎ │   0x000087b1      4489f9         mov ecx, r15d
│ │╎╎╎╎ │   0x000087b4      83e103         and ecx, 3
│ │╎╎╎╎ │   0x000087b7      49630c8e       movsxd rcx, dword [r14 + rcx*4]
│ │╎╎╎╎ │   0x000087bb      4c01f1         add rcx, r14
│ │╎╎╎╎ │   ;-- switch:
│ │╎╎╎╎ │   0x000087be      ffe1           jmp rcx                     ; switch table (4 cases) at 0x490ac
│ │╎╎╎╎ │   ;-- case 0:                                                ; from 0x000087be
│ │╎╎╎╎ │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87be(x)
│ │╎╎╎╎ │   0x000087c0      483b742408     cmp rsi, qword [var_8h]
│ │╎╎╎╎┌──< 0x000087c5      750d           jne 0x87d4
│ │╎╎╎╎││   0x000087c7      4889df         mov rdi, rbx                ; int64_t arg1
│ │╎╎╎╎││   0x000087ca      e841feffff     call sym alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b ; sym.alloc::raw_vec::RawVec_T_A_::grow_one::h4343ba1c9b16889b
│ │╎╎╎╎││                                                              ; alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b
│ │╎╎╎╎││   0x000087cf      488b742418     mov rsi, qword [var_18h]
│ │╎╎╎╎││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87c5(x)
│ │╎╎╎╎└──> 0x000087d4      488b442410     mov rax, qword [var_10h]
│ │╎╎╎╎ │   0x000087d9      4889f2         mov rdx, rsi
│ │╎╎╎╎ │   0x000087dc      48c1e204       shl rdx, 4
│ │╎╎╎╎ │   0x000087e0      488d0c10       lea rcx, [rax + rdx]
│ │╎╎╎╎ │   0x000087e4      c704100000..   mov dword [rax + rdx], 0x3f800000 ; [0x3f800000:4]=-1
│ │╎╎╎╎ │   0x000087eb      f30f100d15..   movss xmm1, dword [0x00049008] ; [0x49008:4]=0x3e4ccccd
│ │╎╎╎╎┌──< 0x000087f3      eb5e           jmp 0x8853
..
│ │╎╎╎╎││   ;-- case 2:                                                ; from 0x000087be
│ │╎╎╎╎││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87be(x)
│ │╎╎╎╎││   0x00008800      483b742408     cmp rsi, qword [var_8h]
│ │╎╎└────< 0x00008805      0f8515ffffff   jne 0x8720
│ │╎╎ ╎││   0x0000880b      4889df         mov rdi, rbx                ; int64_t arg1
│ │╎╎ ╎││   0x0000880e      e8fdfdffff     call sym alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b ; sym.alloc::raw_vec::RawVec_T_A_::grow_one::h4343ba1c9b16889b
│ │╎╎ ╎││                                                              ; alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b
│ │╎╎ ╎││   0x00008813      488b742418     mov rsi, qword [var_18h]
│ │╎╎ └───< 0x00008818      e903ffffff     jmp 0x8720
..
│ │╎╎  ││   ;-- case 3:                                                ; from 0x000087be
│ │╎╎  ││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87be(x)
│ │╎╎  ││   0x00008820      483b742408     cmp rsi, qword [var_8h]
│ │╎╎ ┌───< 0x00008825      7512           jne 0x8839
│ │╎╎ │││   0x00008827      4889df         mov rdi, rbx                ; int64_t arg1
│ │╎╎ │││   0x0000882a      e8e1fdffff     call sym alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b ; sym.alloc::raw_vec::RawVec_T_A_::grow_one::h4343ba1c9b16889b
│ │╎╎ │││                                                              ; alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b
│ │╎╎ │││   0x0000882f      488b442410     mov rax, qword [var_10h]
│ │╎╎ │││   0x00008834      488b742418     mov rsi, qword [var_18h]
│ │╎╎ │││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8825(x)
│ │╎╎ └───> 0x00008839      4889f2         mov rdx, rsi
│ │╎╎  ││   0x0000883c      48c1e204       shl rdx, 4
│ │╎╎  ││   0x00008840      488d0c10       lea rcx, [rax + rdx]
│ │╎╎  ││   0x00008844      c70410db0f..   mov dword [rax + rdx], 0x40490fdb ; [0x40490fdb:4]=-1
│ │╎╎  ││   0x0000884b      f30f100dad..   movss xmm1, dword [segment.LOAD2] ; [0x49000:4]=0x40490fdb
│ │╎╎  ││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87f3(x)
│ │╎╎  └──> 0x00008853      f30f10542404   movss xmm2, dword [var_4h]
│ │╎╎   │   0x00008859      0f28c2         movaps xmm0, xmm2
│ │└──────< 0x0000885c      e9ebfeffff     jmp 0x874c
..
│ │ ╎   │   ;-- case 1:                                                ; from 0x000087be
│ │ ╎   │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x87be(x)
│ │ ╎   │   0x00008870      483b742408     cmp rsi, qword [var_8h]
│ │ ╎  ┌──< 0x00008875      750d           jne 0x8884
│ │ ╎  ││   0x00008877      4889df         mov rdi, rbx                ; int64_t arg1
│ │ ╎  ││   0x0000887a      e891fdffff     call sym alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b ; sym.alloc::raw_vec::RawVec_T_A_::grow_one::h4343ba1c9b16889b
│ │ ╎  ││                                                              ; alloc::raw_vec::RawVec<T,A>::grow_one::h4343ba1c9b16889b
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
│  ││││ │   0x00008982      0fc6c055       shufps xmm0, xmm0, 0x55
│  ││││ │   0x00008986      f30f58c1       addss xmm0, xmm1
│  ││││ │   0x0000898a      f30f1144243c   movss dword [var_3ch], xmm0
│  ││││ │   0x00008990      488d44243c     lea rax, [var_3ch]
│  ││││ │   0x00008995      4889442440     mov qword [var_40h], rax
│  ││││ │   0x0000899a      488d051fe9..   lea rax, [sym.core::fmt::float::__impl_core::fmt::Display_for_f32_::fmt::h566d1f599f294c14] ; 0x472c0
│  ││││ │   0x000089a1      4889442448     mov qword [var_48h], rax
│  ││││ │   0x000089a6      488d056304..   lea rax, [0x00058e10]
│  ││││ │   0x000089ad      4889442408     mov qword [var_8h], rax
│  ││││ │   0x000089b2      48c7442410..   mov qword [var_10h], 2
│  ││││ │   0x000089bb      48c7442428..   mov qword [var_28h], 0
│  ││││ │   0x000089c4      488d442440     lea rax, [var_40h]
│  ││││ │   0x000089c9      4889442418     mov qword [var_18h], rax
│  ││││ │   0x000089ce      48c7442420..   mov qword [var_20h], 1
│  ││││ │   0x000089d7      488d7c2408     lea rdi, [var_8h]
│  ││││ │   0x000089dc      ff15ae320500   call qword [sym.std::io::stdio::_print::h9f0d4f77f60009bb] ; [0x5bc90:8]=0x206b0 sym.std::io::stdio::_print::h9f0d4f77f60009bb
│  ││││ │   0x000089e2      4885db         test rbx, rbx
│  ││││┌──< 0x000089e5      7415           je 0x89fc
│  ││││││   0x000089e7      48c1e304       shl rbx, 4
│  ││││││   0x000089eb      ba04000000     mov edx, 4
│  ││││││   0x000089f0      4c89f7         mov rdi, r14
│  ││││││   0x000089f3      4889de         mov rsi, rbx
│  ││││││   0x000089f6      ff1594310500   call qword [sym.__rust_dealloc] ; [0x5bb90:8]=0x8ac0 case.0x35315.9
│  ││││││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x89e5(x)
│  ││││└──> 0x000089fc      4883c450       add rsp, 0x50
│  ││││ │   0x00008a00      5b             pop rbx
│  ││││ │   0x00008a01      415e           pop r14
│  ││││ │   0x00008a03      415f           pop r15
│  ││││ │   0x00008a05      c3             ret
│  ││││ │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x88e7(x)
│  │││└───> 0x00008a06      488d152304..   lea rdx, [0x00058e30]
│  │││ ┌──< 0x00008a0d      eb15           jmp 0x8a24
│  │││ ││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x88f4(x)
│  ││└────> 0x00008a0f      488d153204..   lea rdx, [0x00058e48]
│  ││ ┌───< 0x00008a16      eb0c           jmp 0x8a24
│  ││ │││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8901(x)
│  │└─────> 0x00008a18      488d154104..   lea rdx, [0x00058e60]
│  │ ┌────< 0x00008a1f      eb03           jmp 0x8a24
│  │ ││││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x890a(x)
│  └──────> 0x00008a21      4889cf         mov rdi, rcx
│    ││││   ; CODE XREFS from cleancode::main::he34f242c79130c17 @ 0x8a0d(x), 0x8a16(x), 0x8a1f(x)
│    └└└──> 0x00008a24      ff1566350500   call qword [sym.core::panicking::panic_bounds_check::h133b156955eee6fd] ; [0x5bf90:8]=0x7f90 sym.core::panicking::panic_bounds_check::h133b156955eee6fd
│       │   0x00008a2a      0f0b           ud2
│       │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x86e6(x)
│       └─> 0x00008a2c      bf04000000     mov edi, 4
│           0x00008a31      be00800200     mov esi, 0x28000
│           0x00008a36      ff15bc350500   call qword [sym.alloc::raw_vec::handle_error::hfa4d56c5e7760394] ; [0x5bff8:8]=0x7d10 sym.alloc::raw_vec::handle_error::hfa4d56c5e7760394
│           0x00008a3c      4989c7         mov r15, rax
│           0x00008a3f      488b742408     mov rsi, qword [var_8h]
│           0x00008a44      4885f6         test rsi, rsi
│       ┌─< 0x00008a47      742d           je 0x8a76
│       │   0x00008a49      488b7c2410     mov rdi, qword [var_10h]
│       │   0x00008a4e      48c1e604       shl rsi, 4
│       │   0x00008a52      ba04000000     mov edx, 4
│      ┌──< 0x00008a57      eb17           jmp 0x8a70
..
│     │││   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8a57(x)
│     │└──> 0x00008a70      ff151a310500   call qword [sym.__rust_dealloc] ; [0x5bb90:8]=0x8ac0 case.0x35315.9
│     │ │   ; CODE XREF from cleancode::main::he34f242c79130c17 @ 0x8a47(x)
│     │ │   ; CODE XREF from case.0x87be.1 @ +0x1ef(x)
│     └─└─> 0x00008a76      4c89ff         mov rdi, r15
│           0x00008a79      e8c2d5ffff     call sym.imp._Unwind_Resume
└           0x00008a7e      6690           nop

