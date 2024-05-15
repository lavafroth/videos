#!/usr/bin/env manim
# coding: utf-8
from manim import *

class MyScene(Scene):
    def construct(self):
        code = Code(code="""  lo.uid_mappings = lo.uid_str ? read_mappings (lo.uid_str) : NULL;
  lo.gid_mappings = lo.gid_str ? read_mappings (lo.gid_str) : NULL;

  errno = 0;
  if (lo.timeout_str)
    {
      lo.timeout = strtod (lo.timeout_str, NULL);
      if (errno == ERANGE)
        error (EXIT_FAILURE, errno, "cannot convert %s", lo.timeout_str);
    }

  if (lo.plugins == NULL)
    lo.plugins = load_default_plugins ();

  lo.plugins_ctx = load_plugins (lo.plugins);

  layers = read_dirs (&lo, lo.lowerdir, true, NULL);
  if (layers == NULL)
    {
      error (EXIT_FAILURE, errno, "cannot read lower dirs");
    }
""", language='C')[2]
        copy_0 = code[16].copy()
        copy_1 = code[0].copy()
        copy_2 = code[1].copy()
        self.play(FadeIn(code))
        self.wait(2)
        self.play(code.animate.set_opacity(0.75))
        self.play(Write(copy_0))
        self.wait(2)
        self.play(AnimationGroup(
            Write(copy_1), Write(copy_2)
        ))
        self.wait(2)
        self.play(AnimationGroup(
            FadeOut(code),
            FadeOut(copy_0),
            FadeOut(copy_1),
            FadeOut(copy_2),
        ))

        code = Code(code="""if (lo.workdir)
    {
      int dfd;
      cleanup_free char *path = NULL;

      path = realpath (lo.workdir, NULL);
      if (path == NULL)
        goto err_out1;
      mkdir (path, 0700);
      path = realloc (path, strlen (path) + strlen ("/work") + 1);
      if (! path)
        error (EXIT_FAILURE, errno, "allocating workdir path");
      strcat (path, "/work");
      mkdir (path, 0700);
      // SNIP
""", language='C')[2].shift(0.5 * LEFT)
        copy_0 = code[5].copy()
        copy_1 = code[9].copy()
        copy_2 = code[12].copy()
        self.play(FadeIn(code))
        self.wait(2)
        self.play(code.animate.set_opacity(0.75))
        self.play(AnimationGroup(
            Write(copy_0), Write(copy_1), Write(copy_2)
        ))
        self.wait(2)
        self.play(AnimationGroup(
            FadeOut(code),
            FadeOut(copy_0),
            FadeOut(copy_1),
            FadeOut(copy_2),
        ))
        
        code = Code(code="""
  umask (0);
  disable_locking = ! lo.threaded;

  se = fuse_session_new (&args, &ovl_oper, sizeof (ovl_oper), &lo);
  lo.se = se;
  if (se == NULL)
    {
      error (0, errno, "cannot create FUSE session");
      goto err_out1;
    }
  if (fuse_set_signal_handlers (se) != 0)
    {
      error (0, errno, "cannot set signal handler");
      goto err_out2;
    }

  signal (SIGUSR1, print_stats);""", language='C')[2].shift(0.5 * LEFT)
        copy_0 = code[3].copy()
        self.play(FadeIn(code))
        self.wait(2)
        self.play(code.animate.set_opacity(0.75))
        self.play(
            Write(copy_0)
        )
        self.wait(2)
        self.play(AnimationGroup(
            FadeOut(code),
            FadeOut(copy_0),
        ))
