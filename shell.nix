{ pkgs ? import <nixpkgs> {} }:

let
  aocPython = pkgs.python38.buildEnv.override {
    extraLibs = with pkgs.python38Packages; [
      networkx
      numpy
      scipy
    ];
  };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    aocPython
  ];
}
