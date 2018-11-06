# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
Fredkin gate. Controlled-SWAP.
"""
from qiskit import Gate
from qiskit import QuantumCircuit
from qiskit.instructionset import InstructionSet
from qiskit.quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import


class FredkinGate(Gate):
    """Fredkin gate."""

    def __init__(self, ctl, tgt1, tgt2, circ=None):
        """Create new Fredkin gate."""
        super().__init__("cswap", [], [ctl, tgt1, tgt2], circ)

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cswap(self.qargs[0], self.qargs[1], self.qargs[2]))


def cswap(self, ctl, tgt1, tgt2):
    """Apply Fredkin to circuit."""
    if isinstance(ctl, QuantumRegister) and \
       isinstance(tgt1, QuantumRegister) and \
       isinstance(tgt2, QuantumRegister) and \
       len(ctl) == len(tgt1) and len(ctl) == len(tgt2):
        instructions = InstructionSet()
        for i in range(ctl.size):
            instructions.add(self.cswap((ctl, i), (tgt1, i), (tgt2, i)))
        return instructions

    self._check_qubit(ctl)
    self._check_qubit(tgt1)
    self._check_qubit(tgt2)
    self._check_dups([ctl, tgt1, tgt2])
    return self._attach(FredkinGate(ctl, tgt1, tgt2, self))


QuantumCircuit.cswap = cswap
