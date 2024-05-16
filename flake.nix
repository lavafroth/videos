{
  description = "devshell for making lavafroth videos";

  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
  flake-utils.lib.eachDefaultSystem
    (system:
      let pkgs = nixpkgs.legacyPackages.${system}; in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            manim
            ffmpeg
            (writeScriptBin "new" ''
            cat << EOF > "$1.py"
            #!/usr/bin/env manim
            from manim import *
            from hackermanim import *

            class Sc(Scene):
                def construct(self):
                    Text.set_default(font="Poppins")
                    Code.set_default(font="Terminess Nerd Font Propo", style="monokai")
            EOF
            $EDITOR "$1.py"
            '')
          ];
        };
      }
    );
}
