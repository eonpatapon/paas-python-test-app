{
  description = "Flake for python development";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default";
  };

  outputs = inputs@{ flake-parts, systems, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import systems;

      perSystem = { pkgs, ... }: {
        devShells.default = pkgs.mkShellNoCC {
          name = "python-devshell";
          buildInputs = [ pkgs.python310 ];
        };

      };
    };
}
