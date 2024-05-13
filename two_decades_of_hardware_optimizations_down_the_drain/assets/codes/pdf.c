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
