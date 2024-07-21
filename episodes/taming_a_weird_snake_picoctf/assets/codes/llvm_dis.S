sum:
        test    esi, esi
        jle     .LBB0_1
        mov     ecx, esi
        cmp     esi, 32
        jae     .LBB0_4
        xor     edx, edx
        xor     eax, eax
        jmp     .LBB0_12
.LBB0_1:
        xor     eax, eax
        ret
.LBB0_4:
        mov     edx, ecx
        and     edx, -32
        lea     rsi, [rdx - 32]
        mov     rax, rsi
        shr     rax, 5
        inc     rax
        mov     r8d, eax
        and     r8d, 3
        cmp     rsi, 96
        jae     .LBB0_6
        vpxor   xmm0, xmm0, xmm0
        xor     esi, esi
        vpxor   xmm1, xmm1, xmm1
        vpxor   xmm2, xmm2, xmm2
        vpxor   xmm3, xmm3, xmm3
        jmp     .LBB0_8
.LBB0_6:
        and     rax, -4
        vpxor   xmm0, xmm0, xmm0
        xor     esi, esi
        vpxor   xmm1, xmm1, xmm1
        vpxor   xmm2, xmm2, xmm2
        vpxor   xmm3, xmm3, xmm3
.LBB0_7:
        vpaddd  ymm0, ymm0, ymmword ptr [rdi + 4*rsi]
        vpaddd  ymm1, ymm1, ymmword ptr [rdi + 4*rsi + 32]
        vpaddd  ymm2, ymm2, ymmword ptr [rdi + 4*rsi + 64]
        vpaddd  ymm3, ymm3, ymmword ptr [rdi + 4*rsi + 96]
        vpaddd  ymm0, ymm0, ymmword ptr [rdi + 4*rsi + 128]
        vpaddd  ymm1, ymm1, ymmword ptr [rdi + 4*rsi + 160]
        vpaddd  ymm2, ymm2, ymmword ptr [rdi + 4*rsi + 192]
        vpaddd  ymm3, ymm3, ymmword ptr [rdi + 4*rsi + 224]
        vpaddd  ymm0, ymm0, ymmword ptr [rdi + 4*rsi + 256]
        vpaddd  ymm1, ymm1, ymmword ptr [rdi + 4*rsi + 288]
        vpaddd  ymm2, ymm2, ymmword ptr [rdi + 4*rsi + 320]
        vpaddd  ymm3, ymm3, ymmword ptr [rdi + 4*rsi + 352]
        vpaddd  ymm0, ymm0, ymmword ptr [rdi + 4*rsi + 384]
        vpaddd  ymm1, ymm1, ymmword ptr [rdi + 4*rsi + 416]
        vpaddd  ymm2, ymm2, ymmword ptr [rdi + 4*rsi + 448]
        vpaddd  ymm3, ymm3, ymmword ptr [rdi + 4*rsi + 480]
        sub     rsi, -128
        add     rax, -4
        jne     .LBB0_7
