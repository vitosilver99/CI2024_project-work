# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Notez bien: No need to include f0 -- it's just an example!
def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5

def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    safe_div = lambda num, den: np.divide(num, np.where(den != 0, den, 1e-100))
    safe_log = lambda val: np.log(np.maximum(1e-100, val))
    safe_sqrt = lambda val: np.sqrt(np.maximum(0, val))
    safe_cos = lambda val: np.cos(np.clip(val, -1e10, 1e10))
    safe_tan = lambda val: np.tan(np.clip(val, -np.pi/2 + 1e-4, np.pi/2 - 1e-4))

    return (
        np.add(
            np.multiply(
                safe_sqrt(safe_log(safe_cos(safe_log(np.multiply(x[2], x[1]))))), x[0]
            ),
            np.subtract(
                np.subtract(
                    np.subtract(
                        safe_sqrt(
                            np.multiply(
                                np.multiply(
                                    x[0],
                                    np.add(
                                        np.multiply(x[2], x[1]), safe_tan(x[2])
                                    )
                                ),
                                safe_sqrt(safe_log(safe_sqrt(safe_div(x[2], 10.543510297651773))))
                            )
                        ),
                        np.subtract(
                            10.924171372825635,
                            safe_log(
                                np.multiply(
                                    x[0],
                                    np.add(
                                        safe_sqrt(
                                            safe_div(
                                                np.add(x[0], safe_div(1.552613023714905, x[2])),
                                                safe_div(
                                                    np.sin(x[0]),
                                                    safe_sqrt(safe_sqrt(safe_div(-0.7557112491004349, x[0])))
                                                )
                                            )
                                        ),
                                        safe_div(
                                            -47.45540488754337,
                                            safe_sqrt(
                                                safe_sqrt(
                                                    np.multiply(
                                                        np.subtract(
                                                            np.multiply(
                                                                x[0],
                                                                np.add(
                                                                    safe_log(safe_log(np.multiply(x[0], 9.063692540724073))),
                                                                    safe_tan(x[2])
                                                                )
                                                            ),
                                                            safe_sqrt(
                                                                safe_log(
                                                                    np.subtract(
                                                                        np.subtract(
                                                                            safe_sqrt(safe_div(-0.7557112491004349, x[0])),
                                                                            safe_div(-0.7557112491004349, x[0])
                                                                        ),
                                                                        safe_log(
                                                                            np.multiply(
                                                                                np.multiply(x[0], np.multiply(x[2], x[1])),
                                                                                safe_sqrt(
                                                                                    safe_log(
                                                                                        safe_sqrt(
                                                                                            safe_div(
                                                                                                safe_cos(
                                                                                                    safe_log(
                                                                                                        np.multiply(x[2], x[1])
                                                                                                    )
                                                                                                ),
                                                                                                10.543510297651773
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        ),
                                                        -0.05123147968650968
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    -11.679882621926069
                ),
                safe_log(
                    np.multiply(
                        np.multiply(
                            x[0],
                            np.add(
                                safe_log(safe_log(safe_div(-0.7557112491004349, x[0]) * x[1])),
                                safe_tan(x[2])
                            )
                        ),
                        safe_sqrt(safe_log(safe_cos(safe_log(np.multiply(x[2], x[1])))))
                    )
                )
            )
        )
    )

def f3(x: np.ndarray) -> np.ndarray: 
   return np.subtract(
        np.add(
            np.subtract(
                np.multiply(x[0], x[0]),
                np.add(1.1418843909085017, x[2])
            ),
            np.subtract(
                np.sin(
                    np.multiply(
                        1.4708865048241961,
                        np.sin(
                            np.multiply(
                                1.4708865048241961,
                                np.sqrt(
                                    np.maximum(0, np.true_divide(
                                        np.add(0.22273292799471647, x[2]),
                                        np.subtract(
                                            np.cos(
                                                np.add(
                                                    np.sqrt(
                                                        np.maximum(0, np.add(
                                                            np.sqrt(
                                                                np.maximum(0, np.add(
                                                                    np.subtract(
                                                                        np.multiply(x[0], x[0]), 
                                                                        x[2]
                                                                    ), 
                                                                    np.subtract(5.585092387202902, x[2])
                                                                ))
                                                            ), 
                                                            1.4708865048241961
                                                        ))
                                                    ),
                                                    np.cos(
                                                        np.cos(
                                                            np.cos(
                                                                np.sin(
                                                                    np.sqrt(np.maximum(0, x[1]))
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            ),
                                            1.4708865048241961
                                        )
                                    ))
                                )
                            )
                        )
                    )
                ),
                x[2]
            )
        ),
        np.subtract(
            np.multiply(x[1], np.multiply(x[1], x[1])),
            np.add(
                np.subtract(
                    np.multiply(x[0], x[0]),
                    0.5543653734888427
                ),
                np.subtract(5.585092387202902, x[2])
            )
        )
    )

def f4(x: np.ndarray) -> np.ndarray: 
    return np.add(np.sqrt(11.03857004111608), np.multiply(7.246489470867109, np.cos(x[1])))

def f5(x: np.ndarray) -> np.ndarray: 
    return np.divide(
        np.divide(
            np.subtract(
                4.763507446791947,
                np.multiply(
                    np.add(6.366218889989474, x[0]),
                    np.multiply(14.5621393076764, x[1])
                )
            ),
            np.add(
                np.multiply(
                    np.add(
                        11.350143908794207,
                        np.add(0.5746784376176798, np.sqrt(0.24854569754379913))
                    ),
                    np.sqrt(np.maximum(0, np.multiply(x[1], np.cos(x[0]))))
                ),
                1e-10  # Per evitare divisioni per zero
            )
        ),
        np.add(
            np.sqrt(np.maximum(0, np.add(
                np.subtract(
                    np.multiply(np.cos(x[1]), x[1]), 
                    x[1]
                ), 
                -8.401825820036258
            ))),
            1e-10  # Per evitare divisioni per zero
        )
    )

def f6(x: np.ndarray) -> np.ndarray: 
    return np.add(
        np.add(
            np.multiply(np.subtract(x[1], x[0]), 0.6945167491855171), x[1]
        ),
        np.divide(
            np.multiply(
                np.divide(np.subtract(x[1], x[0]), 0.5316369921713702),
                -0.8887837131639956
            ),
            np.divide(
                np.subtract(
                    np.log(
                        np.maximum(1e-100, np.add(np.subtract(x[1], 6.2182907542118135), np.multiply(x[0], 0.6945167491855171)))
                    ),
                    np.divide(
                        np.divide(
                            np.log(
                                np.maximum(1e-100, np.add(
                                    np.subtract(
                                        x[1],
                                        np.multiply(np.subtract(np.sin(np.sin(np.sin(x[0]))), x[1]), 0.6945167491855171)
                                    ),
                                    1.4991471060669044
                                ))
                            ),
                            np.add(
                                np.subtract(x[1], 6.2182907542118135),
                                np.add(
                                    np.divide(np.subtract(x[1], x[0]), 9.56558657963237), 
                                    x[1]
                                )
                            )
                        ),
                        16.896222326564367
                    )
                ),
                np.log(
                    np.maximum(1e-100, np.divide(
                        np.divide(
                            np.multiply(np.subtract(x[1], np.subtract(x[1], x[0])), 0.6945167491855171),
                            6.2182907542118135
                        ),
                        x[0]
                    ))
                )
            )
        )
    )

def f7(x: np.ndarray) -> np.ndarray: 
    safe_div = lambda num, den: np.divide(num, np.where(den != 0, den, 1e-100))
    safe_log = lambda val: np.log(np.maximum(1e-100, val))
    safe_sqrt = lambda val: np.sqrt(np.maximum(0, val))
    safe_cos = lambda val: np.cos(np.clip(val, -1e10, 1e10))
    safe_tan = lambda val: np.tan(np.clip(val, -np.pi/2 + 1e-4, np.pi/2 - 1e-4))

    return np.add(
        np.multiply(
            np.multiply(
                x[0], 
                np.add(
                    safe_tan(safe_cos(np.subtract(
                        safe_div(
                            18.942587401015892,
                            np.add(
                                np.multiply(np.multiply(x[0], 5.309087692328209), x[1]),
                                np.add(
                                    safe_div(x[0], 0.6666078913314124),
                                    np.add(
                                        safe_tan(safe_cos(safe_div(
                                            18.942587401015892,
                                            np.add(
                                                0.09330080325717367,
                                                np.add(
                                                    safe_tan(safe_tan(safe_cos(np.subtract(x[1], x[0])))),
                                                    safe_cos(np.subtract(x[0], 0.7510055024396474))
                                                )
                                            )
                                        ))),
                                        np.subtract(4.855519087488644, np.sin(safe_tan(safe_log(x[0]))))
                                    )
                                )
                            )
                        ),
                        5.309087692328209
                    ))),
                    np.add(
                        np.multiply(np.multiply(x[0], 5.309087692328209), x[1]),
                        np.add(
                            safe_tan(safe_cos(safe_div(
                                np.multiply(
                                    np.multiply(
                                        np.add(
                                            safe_tan(safe_cos(np.subtract(
                                                safe_div(
                                                    18.942587401015892,
                                                    np.add(
                                                        np.multiply(np.multiply(x[0], 5.309087692328209), x[1]),
                                                        np.add(
                                                            x[1],
                                                            safe_cos(np.subtract(
                                                                np.add(
                                                                    np.subtract(6.605917439028706, np.subtract(6.890095078240755, x[0])),
                                                                    safe_div(
                                                                        safe_div(
                                                                            np.multiply(
                                                                                np.multiply(x[0], 5.309087692328209), 
                                                                                x[1]
                                                                            ),
                                                                            safe_sqrt(np.multiply(6.469925521136108, x[1]))
                                                                        ),
                                                                        np.where(x[0] != 0, x[0], 1e-10)
                                                                    )
                                                                ),
                                                                x[0]
                                                            ))
                                                        )
                                                    )
                                                ),
                                                5.309087692328209
                                            ))),
                                            np.add(
                                                np.multiply(np.multiply(x[0], 5.309087692328209), x[1]),
                                                np.add(
                                                    safe_tan(safe_cos(safe_div(
                                                        18.942587401015892,
                                                        safe_sqrt(np.multiply(6.469925521136108, x[1]))
                                                    ))),
                                                    np.subtract(4.855519087488644, np.sin(safe_tan(safe_log(x[0]))))
                                                )
                                            )
                                        ),
                                        5.309087692328209
                                    ),
                                    x[1]
                                ),
                                np.add(
                                    np.multiply(np.multiply(x[0], 5.309087692328209), x[1]),
                                    np.add(
                                        0.09330080325717367,
                                        safe_cos(np.subtract(x[0], np.subtract(safe_cos(x[0]), x[1])))
                                    )
                                )
                            ))),
                            np.subtract(4.855519087488644, np.sin(safe_tan(safe_log(np.subtract(x[1], x[0])))))
                        )
                    )
                )
            ),
            x[1]
        ),
        np.add(
            safe_tan(safe_tan(safe_cos(np.subtract(x[1], x[0])))),
            safe_cos(np.subtract(safe_cos(x[0]), x[1]))
        )
    )

def f8(x: np.ndarray) -> np.ndarray:
    safe_sqrt = lambda val: np.sqrt(np.maximum(0, val))
    safe_sin = lambda val: np.sin(np.clip(val, -1e100, 1e100))

    return np.multiply(
        np.add(
            np.multiply(
                np.multiply(11.262832907882053, x[5]),
                np.add(
                    safe_sin(safe_sqrt(safe_sqrt(np.multiply(
                        np.add(
                            np.multiply(5.257718390320081, np.subtract(x[5], -0.09553543323136982)),
                            safe_sqrt(
                                np.add(
                                    np.multiply(0.0030932378592536795, np.add(
                                        np.add(safe_sqrt(x[5]), np.multiply(
                                            np.multiply(
                                                np.multiply(
                                                    np.multiply(11.262832907882053, x[5]),
                                                    np.add(
                                                        safe_sin(safe_sqrt(safe_sqrt(np.multiply(
                                                            np.add(
                                                                -225.60053506465715,
                                                                safe_sqrt(
                                                                    np.add(
                                                                        np.multiply(
                                                                            11.262832907882053,
                                                                            np.add(
                                                                                np.add(x[3], np.multiply(5.257718390320081, x[5])),
                                                                                np.add(x[3], np.multiply(x[5], x[5]))
                                                                            )
                                                                        ),
                                                                        -225.60053506465715
                                                                    )
                                                                )
                                                            ),
                                                            safe_sqrt(x[5])
                                                        )))),
                                                        np.multiply(11.262832907882053, np.subtract(x[5], safe_sin(safe_sqrt(x[5]))))
                                                    )
                                                ),
                                                x[5]
                                            ),
                                            x[5]
                                        )),
                                        np.add(x[3], np.multiply(11.262832907882053, x[5]))
                                    )),
                                    -225.60053506465715
                                )
                            )
                        ),
                        safe_sqrt(x[5])
                    )))),
                    np.multiply(
                        11.262832907882053,
                        np.subtract(x[5], safe_sin(safe_sqrt(x[5])))
                    )
                )
            ),
            -225.60053506465715
        ),
        x[5]
    )
