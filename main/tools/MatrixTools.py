from numpy.lib.twodim_base import diag, eye
from numpy.linalg import svd, cholesky
from numpy.ma.core import zeros, cos, sin, sqrt, shape
from numpy.random import randn

class MatrixTools(object):
    @staticmethod
    def rotation_matrix(theta):
        """
        Returns a 2d rotation matrix where theta is in radiants
        """
        R = zeros((2, 2))
        R[0, 0] = cos(theta)
        R[0, 1] = -sin(theta)
        R[1, 0] = sin(theta)
        R[1, 1] = cos(theta)
        
        return R
        
    @staticmethod
    def low_rank_approx(K, d):
        """
        Returns a low rank approximation factor L of the given psd matrix such that
        LL^T \approx K with a given number of principal components to use
    
        K - psd matrix to compute low-rank approximation of
        d - number of principal components to use
        
        returns (L, s, V) where
        L - LL^T \approx K
        s - 1D vector of Eigenvalues
        V - matrix containing Eigen-row-vectors
        """
        # perform SVD and only use first d components. Note that U^T=V if K psd and
        # rows of V are Eigenvectors of K
        U, s, V = svd(K)
        U = U[:, 0:d]
        V = V[0:d, :]
        s = s[0:d]
        S = diag(s)
        
        # K \approx=U.dot(S.dot(V))
        L = sqrt(S).dot(V)
        
        # LL^T \approx K
        return (L, s, V)
    
if __name__ == '__main__':
    x = randn(30, 1)
    K = x.T.dot(x) + eye(30)
    L = cholesky(K)
    A = MatrixTools.low_rank_approx(K, 10)
    print shape(A)
    print shape(L)
