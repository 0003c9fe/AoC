{ pkgs ? import <nixpkgs> {} }:

let
  aocPython = pkgs.python38.buildEnv.override {
    extraLibs = with pkgs.python38Packages; [
      jedi
      networkx
      numpy
      pylint
      scipy
    ];
  };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    aocPython
  ];
}
