"""Integrators, e.g. Integrated Brownian motion, integrated Matern, etc.."""

import numpy as np

from probnum.filtsmooth.statespace import sde


class Integrator:
    """
    Integrators are specific SDEs, where each state is a derivative of another state.

    This class has access to things like projection matrices, etc. and is used as a prior
    for ODE solvers. The property of being an integrator is something that every SDE can have.
    To this end, subclass from Integrators additionally to subclassing from
    e.g. sde.LTISDE and Bob's your uncle.
    """

    def proj2coord(self, state_or_rv, coord):
        """Project a state or a random variable to its respective coordinate"""
        raise NotImplementedError

    def proj2coord_matrix(self, coord: int) -> np.ndarray:
        """
        Projection matrix to :math:`i`-th coordinates.

        Computes the matrix

        .. math:: H_i = \\left[ I_d \\otimes e_i \\right] P^{-1},

        where :math:`e_i` is the :math:`i`-th unit vector,
        that projects to the :math:`i`-th coordinate of a vector.
        If the ODE is multidimensional, it projects to **each** of the
        :math:`i`-th coordinates of each ODE dimension.

        Parameters
        ----------
        coord : int
            Coordinate index :math:`i` which to project to.
            Expected to be in range :math:`0 \\leq i \\leq q + 1`.

        Returns
        -------
        np.ndarray, shape=(d, d*(q+1))
            Projection matrix :math:`H_i`.
        """
        raise NotImplementedError


class GeneralMatern(sde.LTISDE, Integrator):
    """
    With matrices W_0, ..., W_q.

    Parameters
    ----------
    weight_matrices :
        Weight matrices W_0, ..., W_q. Shape (q+1, d, d)
    diffusion_matrix :
        Diffusion matrix sqrt(gamma). Shape (d, d).
    """

    def __init__(self, weight_matrices, diffusion_matrix):
        raise NotImplementedError


class TensorMatern(GeneralMatern):
    """W_i = w_i \otimes I_d"""

    pass


class Matern(TensorMatern):
    """Classical Matern process in 1d."""

    pass


class GeneralIOUP(sde.LTISDE, Integrator):
    """With matrix W."""

    pass


class TensorIOUP(GeneralMatern):
    """W = I_d \\otimes w"""

    pass


class IOUP(TensorMatern):
    """Classical IOUP in 1d"""

    pass


class GeneralIBM(sde.LTISDE, Integrator):
    """Multidimensional IBM"""

    pass


class TensorIBM(GeneralIBM):
    """Multidimensional IBM with tensor product structure."""

    pass


class IBM(TensorIBM):
    """IBM in 1d."""

    pass
