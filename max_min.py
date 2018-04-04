######################################################################
#  Computing the MinL2 solution for a sorted sequence
#
#  Input: an array of n numbers, 'stilde', assumed to be noisy observations of a non-decreasing sequence. 
#
#  Output: a non-decreasing sequence, 'sbar', which minimizes the L2 distance between sbar and stilde.
#
#
#  The original theoretical justification for this algorithm was presented in:
#
#  Boosting the Accuracy of Differentially-Private Histograms Through Consistency
#  Michael Hay and Vibhor Rastogi and Gerome Miklau and Dan Suciu
#  International Conference on Very Large Data Bases (VLDB) 2010
#  Preprint, arXiv:0904.0942 2009
#
#  The linear-time algorithm below was originally presented in:
#
#  Accurate Estimation of the Degree Distribution of Private Networks
#  Michael Hay and Chao Li and Gerome Miklau and David Jensen
#  International Conference on Data Mining (ICDM) 2009
# 
#
#  Examples:
#
#  >>> import max_min
#
#  >>> stilde = [1, 9, 4, 3, 4]
#  >>> max_min.max_min(stilde)
#  [1.0, 5.0, 5.0, 5.0, 5.0]     
#
#  >>> stilde=[1,2,3,4,5]
#  >>> max_min.max_min(stilde)
#  [1.0, 2.0, 3.0, 4.0, 5]
#
#  >>> stilde=[5,4,3,2,1]
#  >>> max_min.max_min(stilde)
#  [3.0, 3.0, 3.0, 3.0, 3.0]
#


def max_min(stilde):

    n = len(stilde)
    js = [[1, stilde[-1]]]

    # Backward computing stack js
    for c in range(n-2, -1, -1):
        cur = [1, stilde[c]]

        while ( len(js) > 0 ):
            if ( js[-1][1] * cur[0] > cur[1] ):
                break

            cur[0] = cur[0] + js[-1][0]
            cur[1] = cur[1] + js[-1][0] * js[-1][1]

            js.pop()

        cur[1] = float(cur[1]) / cur[0]
        js.append(cur)

    # Construct sbar from stack js
    sbar = []
    while ( len(js) > 0 ):
        sbar.extend([js[-1][1] for x in range(js[-1][0])])
        js.pop()

    return sbar
