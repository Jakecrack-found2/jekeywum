#bro

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJzsfQtAHMd5/97e+3gKkEBCSCsECCQB9+DgACGJp4R4CAkkJPRAx+0Bh447vHfogQ8bpUosJ0qCYjuWH2qwYydSYjdKa7dO67SKkyZKmqS7yqqi+y9tmtZt1Sdu7Nalj/y/b3dv7w5OSPIjjxa432++nZmdnZmdnZvvm9m5vyKi/jJk96fCKoJ4kqAJWuUlhlU9KhXKpJfokVyyhxRddY9adDU9GtHV9miNsTF1PTrR1ffoRdfQYxBdY49RdE09JtFN6EkQ3cSeRNFN6kkS3eSeZHDV3qQuTE/jTRlO7VmmInw56wl3Wh7BpKsIknATQ+nhItDaL6gI4suq8LGKOEj4dCKrT6kPEidVkyp6S08GnGUaWh6ONUDQCc+rYs/sWQG+iRdUdBIgGZACSAUsA6QB0gEZgOWAFYBMQBZgJWAVIBuwGpADWANYC6AA6wC5gPWAPEA+oACwAVAIKAJsBGwCbAYUA0oApQAzwAKwAmyAMoAdUA6oADgAlYAqQDVgC6AGsBWwDbAdUAuoA9QDGgCNgCbADsBOQDNgF6AF0ApoA7QDdgM6AHsAewGdgC7APsB+QDfgAOAgoAdwCHAYcARwFNALOAZwAvoALgANcAP6AQOAQYAHMAQ4DvAChgE+gB8wAngAwAACgCBgFHACcBJwCnAaMAZ4EBACjAMeAjwMmACcAXwE8GuAs4CPAj4GeARwDvAo4OOATwDOAz4J+BTg04BJwAXAZwCPAR4HPAH4LOBJwEXAU4CnAc8AngVcAvw64HOAKcBzgOcBnwe8AHgR8AXAFwGXAVcAXwJ8GfAS4GXAbwC+ArgK+CrgNwG/BXgF8CrgtwG/A3gN8DXA7wJ+D/A64OuA3wf8AeAa4BuANwDfBHwL8IeAbwO+A7gO+C7ge4A/Anwf8APADwF/DGABHOAG4EcAHnAT8CeAW4BpwJ8CBMD/A/wZYAbw54C/APwY8JeAnwD+CvDXgDcBfwP4W8DfAW4D/h7wD4B/BPwT4J8B/wKYBbwF+FfATwFvA94B/Bvg3wHvAv4DMAf4T8B/Af4b8D+An13AZ58QWSUyKbJaZI3IWpF1F1R7iZ5MkPQ9WcCGnpXAxp5VwKae7AGiZ7WMHOhH1oBvQmzf0UAcmepZC/6JPdT8ngZ8kxb0NevANxli5rpXxIY8Q1wie9ZDaEpPnphSfjgE/FIBy75AQnxSSakA/NJ6NiyImw7ImBe3cEGs5YAV82IVgV9mz0Y39QzGyHKvE92V7vWiu8qd9wzhLhDlbPcG2S2U3SL5nI1QjtSeTe7VU5uJOH/uTfN77fPP3bFmf9RTDP6r49ZsTtyaXdOzPk7ctQviliyoDwqwbl59lN5TWmbwzf2F3rP18e+ZuwRQCjDf5/1L77Hc8f5ZFtw/fpH7ZwX/vLj3Lz/u/Sv4Bd2/Db/Q+1f4gd8/mzvnDvfPtvD+wXlFZ4meMnA39tiBN8FRObibwa2gCadjgHBWAqqgH6wGbAHUQHgxhG8FtwTcbeCWgrsdXDO4tUtjqqUx1YWlMdX/5TGVBfqBOnCt4NYv9QdL/cGFpf7g/3J/YIN+oGGpH1jqBy4s9QP/l/uBMugHGsG1g9sEbjm4O5b6haV+4cJSv/B/uV+ogH5gJ7gOcJvBrQR3F7hV4LaAWw1uK0m4W79AEMSXiYgNA/y2z/ejyU6isEZFELfxuEglaEacwcF2EFQbgdK6Bhm3k+7w+72Np9yu0aCfGds04hmhPL5A0On1Uoz7gVF3IBig+keDo4w7UFNjpbZSpbT7RKlv1Oudy3T5h0v6nS53n99/vMRJB4adPueAm5lbFhPg9QTd87z8jMs5lx7jddwZhLPn0mI8h/HcwnEowpx+R1exxWyxy4LVLAs2RQgHlYV9ysI+dtnHGg4qUwQIMqDgsFSGJWu5dc6IUqW53NwseVaaHVZFsskSJByW7OFQS2VYspnlBCvtZikjVrPshYI57BUQBRv64FXLLGUHdneIfuWVFocoVJgtZlmwhgVbWCgLC3IpKyxmRbDLQvh0a9jHapFyUgFVslf2kqurwma2yUL4NJtVEcJxrOWyEL58mdk+loaC3W6mKMoOosMsX86B+deiYJnTiY50kiOcQ4dFzo/DajV3Sl5lciSxIiUBsqEThR1i5FqxqKIEdWyeM6HU3rB3d3OD6FtnrZCTrbPbbFL1ilJdRGydSw6LPS21ze375Ph25Uy7xSpLFVZZqlBCKyJ+jrAftIawZHM4RKneZpZD623h5lVvg/rdK3vaLBFP615FtHWFw61KuNXqkT3tVrPsCVJz2FNugCjZZalCbrz15RXydRotVodVSrzRYpdrsREqPyJZw5Jd8bOH/crlxgqS3dotedrCbaoR6rJSCkapOSJKF9xht5l3jqE0UGk290t+cJebRGlnZTg7zdCSHLIELUiSysvkqzQ7sJqTJancvLultaujNnLc093a1dUlx7TaHWImmvHZbhiTPcsdsoTPp3Qi5Kyutraua1/0cWv9zt0xx5iwlBzksFFMxOOoCOfaUSE/iM2Vci2h4GiV4lXi8yp7OsyNimitly6BYmO32BCVII8sQmvfIccCsbUFMtYVCWqLiB0RsUs5wb4Pno065QSrozEiNkfE/WHR7uiIiIpveSRupTUi2ndGxFapHiqx4Uie0KM0K6K9XRGVtOAO7IiIBxSxYr+cFjS4MazT4XA33WYvt8teHp9UQe3QcKDzMIhiuGdAyR6WLIqf/OS0w12D3sAgi3bZU6w3gyxaFSkSbI8EOxRPh9TrtDvC3Xy72AHKkkXxs8pSpRKvMtwCO+DK5vru2gOdtWKy4nFbRJQuC6JFyn8HdCFy/lG0K5IjLMmX7VAqpMOOD3mCJFnMBxosYW85Xx3lVrndilKr4mkJSxYloiXs5winrnTJHRW2cDIo1YU9LUqwNRwM960hIraNKeLeiLh/zCCLlrBkkaROG3QtimRVJFtYqgiH2i2OsAR+RlGChuWRPbFByZ52W7csVlSYWyJimyxCcbvls+B+hiW7fCGsSikiSnsVT2tYsinBNnO3Itq6RDGA4slw1EiadqlAEFyu+DkikjWcjsNWF/asDF8RboAcDFKr4mlRPC11ETESblU8rXWKp03xVC4ENzXsaTHXRcT6iNgYEXdExOaI2BoR2yJiu3IFJS8Wa+QK1sgVrEq2w63BDjc3HFweyVZ55FLl5i4lqk2RKhSpMiw5lIQc5gbZExplWFKuA5InLFYolwSxOSKG82mvkFujvVxJqdwczka5UqUgtSielrBkVU6pUCLiFZPD4s6Wup6u2nCkSiVSpdIgHUozBKkhIu6IiJ6I2BoR2yJiV0Tcr4gWj3IFh+JZKXuWQ98l5RKlujr8tlVC5JuMkty2oPRhT4s5fOfLrZXyw9JZLra45LDY013b1izfoXKl0ZTjSCrsaZcfinJ7+KFAqSEiyjeovCJcaSi1RsR2RQy3Oez+5DyAtLOl9kBTrRISvpwjfEdRqouIjRGxNSK2hdMDsa62s3FvJKhDSdCqeFojCYafCRQ9SlSH4umQb1QFdD6NimhTRHu4hVfAYCkshRsZSq2Kp1XxDF8UxHBNg+hQPB3yPa6whSsVpR0RsVUJtyqe4erF/l+qDpRqpSYTfQzDmujjrq7WjsgxfJ1iuDF83BoRwzlVHmCU2hRPq+KpFA9ET0RU8lderkgOJdjRHPZUKgrGsY2KqFSU3XEgLIV77IqKcGtBKXwdR2U4dZDk1B1KP4SjU1kqDzftLtBGKsVhUpelzCwL8J2CatR+h1N2pWayvz7cTPa3wVmdYuxui80iC/AFhMIBh+xzwKH4VJhloVLKwUEcBDMJBEEwiUhJSMlIKUipSMuQ0pBwQSuD63EZXKjCrEDKRMpCWom0CikbaTVSDtIapLVIFNI6pFyk9Uh5SLj0hClA2oBUiFSEtBFpExKuEWGKkUqQSpHMSBYkK5INqQzJjlSOVAE0l7pD1nfD2i7jwLBKpCqkaqQtSDVIW5G2IW1HqkWqQ6pHakBqRGpC2oG0E6kZaRdSC1IrUhtSO9JupA6kPUh7kTqRupD2Ie1H6kY6gHQQqQfpENJhpCNIR5F6kY4hOZH6kFxINJIbqR9pAGkQyYM0hHQcyYs0jORD8iONID2AxCAFkIJIo0gnwpUpamU7ZJ2MOYlhp5BOI40hPYgUQhpHegjpYaQJpDNIH0H6NaSzSB9F+hjSI0jnkB5F+jjSJ5DOI30SMyFpG2ElQ1RymE9h6KeRJpEuROLZzBENxxzRcCzNzGcw5mNIj0eiw5PKPIF+n0V6Euki0lNITyM9g/Qs0iWkX0f6HNJUOBVROWGeQ7/nkT6P9ALSi0hoAmS+iHQZ6QrSl5DQLsi8hPQy0m8gfQXpKtJXkX4T6beQXkF6NXzJDlScmN+OHIICwPwORnkN6WtIv4v0e0ivI30d6feR/gDpGtI3kN5A+ibSt5D+EEjQd9a2de5r3yFoWtsOlgk65Ir9gq6trc5a2SK7beC/94DVWi+7ELu9rckq6JDLD8zpJbcaPPY2VILOpJfc6jlDZ8fO4tYKq1nQNbe1VpS1oNtWUd4gaHc17LFVCrpdnZ0W+y5we3bbIVjTsrsLsoFcuXMuAd3OtuIuGF2AZ9c+R1kHpNlWXAu3s2nOGJb2KZ47RWmH3WZtkqRKjChJVkVCe4dekuyyl10O3GWzyimLUrviuVOR2qRg0OrCwRVmi3R2e6VoQsMsW0A/EwUrWgslQfGxy4JDDrKFI9sscpDdGhbCZ9nDZ9ntYaFcDqowyz4ORYAq1w4GgyMBQTfgCQ6O9gm6JifjOe0UdMN9zoDH5UmFbnlsTZt/zOP1OkvtJWaqsNXjGz1VTe2rpmp9NOP30EUGQVUuqCoElUNQVQok3AbSYgFYATBcprpai4PeamqspHZkxOvudve1eIKldltFia2cKmzZ2dXWupnyeo67qR1u13F/EVU/yPiH3aW3sVu9jZ2aoDJ7BuE7yZMH30S38UviNj6hYxlt/j6P1011Ovsh23KScypqjISrkUXUnKpkLDde5uWcU+Ul5hJLdZGeMamgsScgJSIlISUjpSClAo1tcvuKRwPVlMVcTXUVy1cePt3lH3UNUrYdVKfXQ7upulGPly4tWiWoagVVnaCqF1QNgqpRUDUJqh2CaqegahZUuwRVi6BqFVRtgqpdUO0WVB2Cao+g2iuoOgVVl6DaJ6j2C6puQXVAUB0UVD23cTGk52/VkI2q+6tERyUUscwGTmXlWPr8+rKVWMbWx1RQt8dH+08GqPYuqBxLNdW9u7u8rKjIKKjKBJX9XuqJqu3c19nbbDaXN8i1sbdlj6XECsqE1VpihuF2zyJFCLhH3EzQM68UdshbidXhsJU4KmLvNlS72zPi8zCl5SXWEttYXrwmEYlkK7FDOvhtqfwZAFCxxE8/pcP3jIKqSFBQHZGHlPWwsbM4sWtV73i2Ii92Nn6BjhO0akpDxPkLzYs9rgomRF1Bp1w3OeL7DEGTwdSYY3UwLeZYc0kXm+6QSbkCGVMG5WoL32sKrozEo3WLhuoXC71ELHqu4X2ca1wQmh1VNqXOaNP7uEZCSIX38H2kkPhzyGXSPV4jeUG8+K0hZV6LS72kvs/cxb/+skVLkXaPqaTPj2ckPvTnRh1ShdQnYCAfk+OM91zu99UnjWvutWZoojO2jpcvegdWvOfy3Fs7yrykvsPzdK/XWRsVT7mbC2bhodTr7zl2MDeqBrKOi3eAyY+ul2BeRF6Qow1RYfNSPijmRGLp7dCile3vYFX95GOfmVNXlZbOaUtc/uHSuUyL1Vp6wjNS2uf195UOOz2+UmdJ8FRwTEe5vG4nM3oTspV9yFJdWTFsQtdWMfyTz57DzxNPUrKkfCJeIEXE+dHC/uEEKfwL+14IC4//5IlJ/MxL5YkLVFSMS/Njy59L0WnPT3p+Rhb4iynHKV1sDdxDpmP9F1TS4wuy+5Mnno6bmUjhF17zwv1UNV4gtqYUr0tURFzMb3J+VYcTL77PPyVTTfIikCoq8rfLCSPQ7lElzn43E/D4fVR0HMpSUvFeLz6Wb6TEU63QRpqa93Z2UTsau6jajo69u/c3toYvO1YfidW1s7mT6tq9u7WTAqGjtrmB6txNHdy9j2pvbGyIPr1BSlFOxDTmER8hTINy+X1BxukKUrX0sMdHBf0wtD1NBQc9AarL7/cGqPf3N/D0U/j3tW1jmVK+RV/I416Kamk8CNU3tkkMsGBm6nd3HJQCMay2HQrUCNS1m6ptaGtup6ixUqgcv9frPynnN3yrqOaGzfP/8EqMDUfuxlP0QLF/xO2jxijobU6ePBlZ6IP9TsAZLAkMOgc9vtPB29jxjR3KPmSutpVBpup3Nta3NLfvkPJVi/VZ21oS/XffdSL1iz/eNpYTuQ+RUst3bJVcM1Iw1elnmNNUHeOnDvpHGarFfZry+eGujTD+E24aIheJsdw+mhpxnh52+4J4L6VKcoLngDtIOTGy0zuWg3XgLAH1Y5PDYbaUW+wAs718W9B9KlgjGHp7seft7S3KENSBICOQ/oCghwTcox5aMIDg9Q94fIJmyA9sCK/VEtQQIqiDTp+gRk1b7fR5BA0mKegCpwNB97CgHWE8viB4eobdgjbgdbtH4AqnA4LGfcoD/j4n+Gsgdb+QAEUY7XWOgOJ3+opW0IzitUmALuBmTrgZwYD6fb1zEC45HBgIaKFGxdqF6wb8TAdqbUho5AzMwD2dIGaMiZ/ce77n0cPnD3PGVbxx1aXOF9NeyH4u54UcLqeUzynljKUTedP6xEfGPjI2mcfpM3l95kTuTEL6+S2XbGxWM3xelN2XOyUXPlzCLh4/uycK3jEQau3ZonPNHLmCJ1ew5IoZUj9LJBi3vkUkqLe9jTSL9E4WoTawhgqOdPCkgyUdEO+c+szGsxsnNoLIGvZx5H6e3M+S++eHnOTIUzx5iiVP3Tw9/jY0VVUDOUsQTWQz+RYe7SLflpxZyZl/fv5UH2co5MginixiyaL5wZUcWcWTVSxZ9fWy16uuub627fVtr22bH6uKI6t5spolq7/e8Pquaw98re31ttfaZkjN2SI2seaSGkj6cORWntzKklujUvhk1/mei6pHj5w/cu6ImJqHI4d4coglh24e9/PHR9mTY9zxB/njD7LHH5wl09TpMymZ50OXAuzqNvi8KLuvpksufLiUdh4/nRM7p/XGcwcmHpp4aEaXwCaWcjozrzOzOvOrGa+seq32qzmv5FzNmUlMeYJ83HQh8fFELjGHT8yZcM3oTGeHJtPP+M/6J/zTOtME/Y6O0CdiCXRbed1WVrdVTNDB6Sp5XSWrqxSrx/m1mtdrXquZ0RnOetjUrZfqgaTPawyXWsvp6nhdHaurk5Jfdmb47PDE8IzOeHbwzNDZoQnx/91ZUgNF1OjP7jyz6+yuiV0z+oRzYzf0K1n9yhmt6ZNlZw6dPTRxaEabeubI2SMT8v+sljCsYsVI7777bgCnL75jq0ts2UJ8T1VbCc4fbakl2zTq0eXqeSMme+wA5wMaNpV9iMMme/y03/O4iaJM8pfoBz9yCqdt+5DHTvbhD2PodLevrl/o2MoRGUQHgs7gaKCK6nB66PeapRhbmVrGT1HFibWV0ap42mQR2S5Ye+/7r0jFNENKV4ifiupVN8iC1uvxuU8xh0HGKaIATk/Ct5Uh6Vz/o0nnk86J/8whCI6f5f0LsjykyAszH9RGKXS6iHynQmpFxatIw2zFr9SdSFgCZjdSDxLmTCwJczRMOMEVWCeXw3TeOFnIGbJ5QzZryIZyfZJ+NOF8wjnxf5FyHb2HWxETSi6mjsdTjovU7WPLYdCEAwqq1e+kPT55TDe2gmoadR3HwRZVd3rEGQhQ+2DgQRWRUunbFpZe0PXDGW6aOQYHOPcWKJEqQKVj9Ws41VpetZZVrYUxAnzn6ddyKopXUayKejHjuRUvrJgS/xfWhmLE3U8uGXHFlKKMuB+QwUt7Dwav3PdrqhJNUO/X3JUZOeeOxp4og81Q0p1ixxhjdO1MBbZiB1IlUhVqTXGMMX1ojClKZvDVDqlD2Ia0HakWqQ6pHqkBqRGpCWkHEj4ZTKvy/OwBigzcpYdI7Tp+iulT4X2BwH8hpC4k4ZN153c92nq+lTOs5A0rL9W/SL6Q8FzSC0nc6hJ+dQlnKJnImNYlPDL0kaHJDE63gtetmEibMaWd33xpPZu5Ez4vyu7L9ZILH87UzOOnfWLFLGkkk2eSlp8/fKmTXdUCnxdl9+WA5MKHS2rl8bNnonBaqz/nmDg6cXSBTjFhm1brJ8reXOg/ozaecZx1TIj/MOhTwRXVurOOM1VnqybkfxzK4ZqUN4y1yxtSiW9SJcDfSl3eUKiO3yu8pJ/fKyww60W1szj9Z3Towv4z6rtiQbr6qDPnmcXHoTegNfDUJAeNd04B4mjFOAmLxtGdICbVjHPRMkbnRT+/H4JeIikSHlLRhthtYKaizr7TNaYMd48zTvqK1xPRfUsewVDz6njhZM3ySOjCp9SnOSk/pTGpLJwkia6BeZsBjasHoO+AWojqPWLiz5uamXe21mfEfoVOGtdGtveLyc3C6ZSoPig0b0qtgTiyaVwX0kxF3ZM75CslpKOT8Fsn3tTLgq10NsfkaaHJfLEa0of0dBq0xezg6kis+DlcOLngW3UPZy2cIokyytPLX5o35WAnxg2Ltvh1kbDg+ogcIhe9l8aYOsoMGbF26ayQGjdAizshER1/5aKhqxYNzb6fviVENhCTqiOt46aQaSrqeYpKb3VseofhaR5PGE8MacaTQmo6B+7lmpBhKj3eucHCiBxKCCWGkr4AI5ovK6MaaEvbII01i6ax8a5pOCGNtYumsfmuafwapEEtmkbJXdN4EdJYt2ga5rum8R1II3fRNKx3TeM2pLEe0lh7xzTK7pbGpOp8IqSSt2gq5feQSul7r084u13cfhX+Y79HwmMwCxHQnCSlfhL7cJUcImoc+e1jqdQhyxGqHxdzuLx+n5saM1KHzEeoxlOe4JiJqh/0e1xuUH6LSEFjtlRaBZ3Daq6wWfG4wlppE/TmCqvD6rAVaQWVRSDNFmmRykocP6mcY5lUx2hQSh/fupXV4ypKUDFjK6km9Pf6Xc4gqthoQ+73j/poamyjmK02d3DQT1MWykQdsiqH1kKXf9jjG6ACfr+vCDMMufQH3FVod97pP0kNO32nKVSTTvoZOkDRfuo0aE4nnZIZ2knT1DbZFr8xPH/hPjVSBblkAkHK6wwEN4MYDISlQNBitY0liyUJJ0uNkXC9fKpBThxt3IFBuLhrhHK6XFCK4Daq8HSprwjqDqrGxxRgjZA+v0C27xZUVsYr1tDp27h+94pKSBh2nuqFlI+7mcBcFtXlDzq94ZSg/uWMjmVDXciVKFfHVuV4rDhskwD1kOr3egYGg9Swn3ZTbtApT1M2qLXRoDsgx5JLD9E7nSfcNOXxYVEY6WaVBmiXk6FL0RxSvPv4vcet75hThUAzHcRW4AEC2S8W3YyNRmUDwQZ+ZZJfGYh2SbSDaJLEchATJLECxERJdBStlrR6UetFE4Wg9fhGRoMC2UcL6oFhr6DBiRVBgy90C6bAiNcTRHtGQFiGLa3dH2zC5tXIMH5GHPULapwC0DJO34Bb0DlH4GRIaMQ1ImiCDGjPNWIcLySpFRMTdIHRvmFw1f39fYLaOeIRNCBZBA2IFlG2iVwmcoXIjqJkgcS5BKwsgez3C5rh4CAtaCHFQFAwjAR6vR5MVOURSNcpIdHFOF3He+UrGYPYEno9dEDQjILWD1kGUYuzEwE4F5ojphJAJTPWPCapMJohuCnM51Vo5gEd5oBGtgKcyTybOZH5JpoDVnGqbF6VzaqywX8ixKkyeFUGq8pQYs1ojOeKOU0Wr8maSJvW6FjTalaDnxlScybvbN5EXqyn9kz+2fyJfNEzl9XkcprcGVJ/ZsPZDRMbZozJbMpmzljMG4sn8tDabJoxJJ7rmlz/aPL55FuG7BuGbM6QwxtybhkKbxgKOcNG3rBxwjphfXfGuGqWINWmCM2oDawxn1MX8OoCVl0wo9afKT9bPiH+z2ohAqgw7+jE2Y1yjqzgyQqWrJjRJ547zOlX8fpVkHGDaSJ/llSrU2aSlz2Rz2Y1cGmNfFojl9zEJzeFlSN1ynRSsqwrvfuuOE3g4MhKnqxkycqZhNTJrEe3nd82S6jUFpEmnNNqwyNbPrLlCS27omTqgcvLnguAIH241FI+tZRTm3m1mRU/YoJmjrTwpIUlLTNa07ktnDaL12ZN5IJyxybkslr8gIb2SNVHqs7RnDqdV6ez4ufNBZ4z+oSLJKvP5vTZvD57llittl4MQVWdqThbMVExk5L2hG2SuVDxeMWjofOhiUqxEjdcNnJGC2s9wnYfQrYe4YxHOPVRXn2UVR8Vo2zj1Nt59XZWvV08dHDqSl5dyaorFx5KV5pOWTZLZGisbyFNBKdTM540fcZ0sYxLpfhU6kzzRP057XRKBk6TJJwbk6YPprXLbmmzbmizLqVf7JxaPnWK05p5rZkVP9PGpMlVrDEbPvcfL+Oiayr/soHTWnithRU/v9TxuHuP9+PFAmeLoPZnl0EjEFuCSG8hvU3E+N2RoMXfJZaF0K6HxzyAr4q8saysXkd8U7eh3qz+ZqkK+FsZqxssxLcsmoYK9Xc27UjerVf/sV6zO0H/x8kqYFfUwDxiSnhIMiVEBUXMyFMkEeePVkUbkKNV/aApIscO1PvJMV0cNSP+VaNSj0qPmKcKpUSda4gfa1xtBMV/KiqHUaWYpzLR6oj2imrzPZ+niTovrDRro5VmUHpN8VKal1ddSHtP8fSimkQeuTJugOFsQrwzaFC05xk74sfTg5p+L/EMId09xTOG9LHxQPWMa5iMVp3nKasmD0Gb6ITHVHQinQScTKcAp9LLgNPodOAMejnwCjoTOEvklSET8Co6G3g1nQO8hl4LTIlnraNzgdfTecD5dMFjqvGEkHoqqv1ElWBDCM0OhfPNDuOJ0ar30DIlflEwP+IfSoz8VsI8hTy29jKIOH+0Zp7ZPv4VN354VwwR9CZ6c8hIFz+rQ4V6anncs0pCSXRpKOElc6ySNJ4cUg+tUK6YGe/ceea1rLvHGU+hLaEUUP2+fr+pj6fS1qmV8eLhroj3nddVd4/TsLghf1mwIioPZSEiZLxDv1gZFc9Ol8+7l3F7Zbh3FWjKkY07jrhmnaj+ZSonfirzz1ERviBdKd4BH10V3BKJCz6umBJVh8TJInpLVD5q4uYjunxbP8DybX1P5dMAyEny/Jd9JetjJpGGKEVSnsU8gsmEKzVGxVIMcfS2OL+PEjHlRn2v0Zox6AudatE4sL19zpyUFFb7DqEeYTllKd7f3HGEyg+EZIV0d0tVcX4grIJiJggGa0rUrwVt7eCwGzSdJlSiBU0rKNSCtl86QO1a0Oz0B4JzycMxS+Dmkk943CdH/Eyw+KSHDg4K6kqHec4YcLuKXYPFo865ulyqHdebVdeB5kbnVp+oya2szN1M5YovsnhGh0Uvi9mMfjv8/gFQUqV3XJSAuVQlueJh8WWWOXKbZS4t4jvidQb7/czwnDFXfpEpdy5bDh5h3P2gpxe7/F4/UxxwDbpxDZmocAtq2hcUtd+5laMjA4yTdhd7fHDeKOMuDi9PmzOhKlfsHHCD+qkDLd89Epz7c1yeVjoYHPZuBk3U65GsIqWn0GfTqfm+w97qB2rMJZWbPcOQTKnzhKdfFk+6+0bCviO+gc0bD+H1mSCo7X2nKdfp4KBfXFvpPIEvZ0F9iwv0XF4/RDpSek+RA0EnEzyyUcyBIyZfAc+Az00Xu0+5BlGphurus0kZnUvGyut3B6H+Ap4g6MM+v88d7YumCsHgg6IMOIMxIVhb0ce0GxVn2u8axezMpUg1WOz2ufy0xzcwt2xgzDOymaLd/XAT3ZupPkaJ44VsjULdzCW7fcX7Oje7fXL2qsV39KpKS/sZtzt2Saa4xBA3fPO43MV9zoCbLg3bgUq3jXromrmign6v/2SNGLHX5+8d8fgKoI0EGFcN7YbWArXjpgt6GZqZy0LVvSbXG6BzqRNO7yjIhSUbtxXlzq2WQoacY34o3/zQknD+pJcG4+Uw4DzhLpayWSokRmfmik5QwxUFvZy4oMYljBofLojUYNZxU7xAYK7pvioBMuihoWTFkdoIDPZ5a8xNV9SCBkKcQooTF8j2Mm7aA7UQDAj6QTc8EkxA0Ll6xduqqnZFzS0QaInHwcNP8Q2AJ4kB6ByPJIoWddU4GVI9o6KJEPmM6pL6Ank+qZO4oppT1YiLH+CSZIlZUB93nxa0YtUFUJUIW0LmTFvQUAIlGdk6ltnf31eyBQ2P3sDWkkjAz/DC+GUyQcwSRFk9Gc1cRw/b0cnu67mmFv/3XdvH2lsWxhPXTcxly32nVe47i3e3YL9JhYDm0sMmMzkEZ7IZ1DWYUTxXZRJM0Ke4jo/4PdCZjKBfFqZnc1Tbqy3W8nCa9dAXz6khzTm9vKxuXtL1HZj0bRxnXckTZ7sFXSBI+0ehHz7JiE+h1+8fYT4uGrr8xwPQPXtHA4Pi3Lmg73QHcPET8wmxM4cb6WYEPeOGrtHlFnTY+fqH4UaKRmJBMwrdmTjfLpCMG9fGOhnXoDQ9v0NMYIDxj45AS4M+X9C7oGF50IY14A720h4XNES4dQFx6l7QQtaGA5Kh7wzSI0jnxFy6RgKCCToYeJohbwEhpd7v80HbggPJsrcL47Zgk0hjplB+Dul5sUQBuURX0OtLYl4hOfVIwIr2ueMMiM6AQI46BQ02VEEnrTAWdB4aG7lgwHbidUPF6TrFRdqCxgXlgLyPHvcE0oj5VjjFEsd8Mky4DWVgpRYb2ZuGhPOmW4asG4YsdmX3zYNHbh513uxzc0f7+aP97IEBbuUAZxjkDYOsYfCmx8t7Arc8p294TnOeB3nPg6znwZm0VXxaLpeWx6flndPPkuuNa6ezcj6X8HTCVAOXVcRnFV1ex2dtntTOkuplG6bX5n3uwacfvFzGrTXza81Xl/FrbRc1FzVo48LQAjyAw3ffnV6+6slDnzl04cjjRybJ6RWrnhz6zNAF7+PeSfX06rxZYuWyoreQJhum1+R+zvu097LjaiO3popfU3VrTd2NNXXXKq6XcWs6+DUdt9YcuLHmAHvQyfbR3Bo3v8Z9a83wjTXDrG+UPXGaWzPGrxm7qJ7JXvdszcsZXHYJn11ykZwlCeqBhCkdW+iAZwpEtmrX9UZZ7DwKglPlJqVj4AHyNB48SD4c8atV71ODs1/tVCt+LvV2DTh1mmaN4tei6cCDvZp9Eb9uDYMHQc3JiN9pTaMWnB3aZm3kXG0nHuzTjhoUv5OGHUZwmo27jYrfHqMTD1zG4Yif3/gwHtSaGk2K3w5TNx4cNLkifm7TCTw4ZWpJUPzaEo6icyxhRPa7qJleV/jF7Oez4bCkh2SP+yQhmt8iiNxDuB4b+KJuZkPRC6dZS+sPXOzeA/zeI1z7Ub79KLehl9/Qe2uD+8YGN9s/wG0Y5DcM3gyM8oEQJPKQ6gj5DkH0kn2YpIv0YGou0odJ95J+PELnLVzbNYJH6Pw7OifIf5UcrCDylBTltBRFvHXb1fV4m1rUD6JTr9mDFX9QcxiddUdlvqibXr/xi1ue38KaT+M5ZBOe2k0eRscN2ZnaAgnnDWG6wBcN0KKfffjW2oobayu4tZX82spba7feWLuVW7udX7sdUsteP3WCzS6Gz3T+5hd6b+XX3Miv4fK38fnbpjTThZu/+ODzD0b37OxRN390+NbREzeOnuCOnuKPnrp19KEbRx/C8qtqxfKDI8V9S+S3w3JhA8rAU5oZKp8taL5uux64XsQVdHJUF091sVTXDJXH5le/Bh61PFV7i9pxg9pxXX29/rt6+Nr5bgLbdYDbeYCjDvLUQZY6+Ca1/oum502Xbc+lvJAylTJN5U9pp3OKLu9nc2zwmV5f8PL6qaqpqpnCYrak/XqAK9nLdh7gSuBRPMyVHGaPeLgSD1c4xBcOsYVDM4Wb2eL6a51cYTNf2HyrcPeNwt34ZdfVzXV0swcOcR2H2MPHuI5jXKGTL3Syhc6Zwk1fMX3JdNV2JeWllMsp04XFl7U/RvpLqvDdd2dSMvmUXD7FOkuojGsjNJOa8bjpovVC8uPJk+L/rBp8ocN505B4zvmo/pwG/3+KW9J8oyS7XUu8YcquKyDeyFehXKCp26x+Y2PLKjj4obaw3az+YakKeMmGGFOKJRvikg1xYQmWbIhLNsT4eV2yIS7ZEIkPy4a4eaEN8Z7thwxelPki0mUkRWljMCdj6XEsIczLGPwbSF9Buor0VaTfRPotpFeQXkX6baTfQRKXq7yG9DWk30X6PaTXkb6O9PtIf4B0DekbSG8gfRPpW0h/iPRtzFvN3a01i9iTmOuY0HeRvof0R0jfR/oB2gJ23mfid7bTMDcx0T9FEoDejyWG+TNV+DWUPweKMb4wP8E6ycKlMvHMLhsxyl+pwi+w/DXSm0iKSYT5G6S/RUJrCPN3SLhfE/P3SP+A9I9I/4SkgUwuqot/OkwZmNNVC3Xxzpv7Dt7sQXWc6+nje/rYLhe30sUZaN5Aswb6pnuQd/tvuUdvuEc590nefZJ1n/xfrIufEHXxGlQ2TySw23aze/bL8gEXCP2qIVI6BvaSD0kaXYNa8WtS9+DBIXV/xG9Q3Yh63Q5Nu0bx65C08G5NT8TvsKSFn9aEIn4PaXah4t2qbddGztUewIMe7ZhB8QsZWlHJbjd2GRW//cZ+PBg0MhG/oLEBlewm0y6T4tdqOowHR02DEb8h04N4MG7qSFD89ia4RD09YVT2i1HGD5Ps8IgkRDMq40dEZfzIr74yjjpyHbkTTz1IHiVFg8xxWRn3isq491dOGX/zvpTxmf/FyjiTRqLlLOqLYUnDXtKwlzTshSVY0rCXNOz4eV3SsJc0bOJD0rCZDCjzfSnOzEtIvxyKMvMdpEXVXYYH+vlrqrZ4mmrnz1tTvRAmnEaPN2u8pKkuzRovzRovzRovzRovKaoLS7GkqC4pqgtLsKSoLimq8fO6pKguKarEh6Wovqj6FVZUxxzhSdeRD3Qyl1lO/iK027J42u34z1u7/UyYBu6g3S6tiV7Sbj8I7babZAePS0I0o3Z7QNRuD/zqa7f/G6dhl7TbO2u3qGeI2u20Eb8XjL+C+i3on3H3O1xUb5X03Xs7L1pv1Uh6a0g9ronSW1HPVB/5n3EtaKZx91WktaAjxNWS542DY8d38dPShdT3FE8P+vQHdU3DAj05fjxjSHVP8Ux3shoslrdxXfTektG7Pw4lKikn0ImxZ827m+L+i3dMR9G7UZteLJ1FU7nn3Ig7EOvvIR01nbpYOuOGmPOUkXlwTcR3wc6J8c+g7niG6b7PSLiHel5Gpy1askQ6PTqV0Ly9PZ8h6IyYcNOC8OUx4QkLwlfEhOsXhGfGhBsWhGddSqBXirrWqrvEzI4JNy4IX32XkuRc0ostJimmXqN2yxxS9pZcVL9Ofp/np3gIek0IrU1rQwRaj0K6eNYjegNdKMpFwBvpTcCb6WLgEpFLRTbTFmArbQMuE61TdjHlcroC2EFX0lXPki+qxlPhmtX0FvCrobcCb6O3A9fSdcD1dANwI90EvIPeCdxM7wJuoVuB2+h24N10B/Aeei9wJ90FvI/eD9xNHwA+SPcAHxJjFtOH6SP00WfVcNVldO94WvRPgQ0p9qFQWig1tIw+9pIz1rozpNTteHqwOOpMpf2H5u24Op5B94UyRCuBJRKfdslWAlrU5nWi7I6rzduizuqnB+7RSjAYla7nrlaQuFaduFaCMXoolEEfj3xrihYRb/Q+lgvKOvyeyur7AMvqeE9l1Uyqz//PpOY8cSebxXoiWBAJGVJsLUNKz5xHMFlw/W1RsSglJf9CO4m473pdJDacnzC+HP3Hlz+0XNqXE6WTqrA9pWgk/gS/aCgR7SaitQSNJ4Km3TnsZtpBvI2/Nn57E0Sf05aY4f82fmHfxrt2+2fffbr6Npb4Nnbkc2sbnCc8x0utJRb8YVrx1x+if3aYmtNhAtXUnF7+ndm5ZdShprra9tKmurLaapD2l87pwK2T3Ya20rm8B2m3L+AJnq6xlpg3i5t41FRYzZsH3bhFRo3F6jCPV4+lNtW11pe6fb37OuG8vXB+Cbj1e0vb/Cc8uMUEHLU1lQacw4FR3wBeoiHqoKNdvh6ctwnczv2lFZDRprrdHaUWTKe21MkMu519nuITFc4qWa4+ImictIcWtO5hp8cr7aCIthp8r9yL2z6OuoVUF+OGAgQ9Tm+gN3h6xC1kS/adXtG+0yvtrKCcqQv4RxmXW0hbGElY5sZX0ntpdxCuJqWV0TcaDPp9vSc9wcFe2hNw9nlxjxQpvg63HHEGBc1QwO8TsgbcPjfjDLp75ffWe+W35kXrVlSw0+f0ng56XIFel9fpGRbSlZBhp2sQbmov/lqVaPFxQ9GxyoV0l9cDhewVtxhlToNLuwUSAnRSOQSjXB48dVjcbHTO5BwNDpZIWU1EGWsJN7eYs7n8Ubu4yBuXSjFLRhh/0O/ye0ua+sqctXDWTid0Km7mCilk9ffhD2v1Mu4HevsZyA/tPd0r/vRWuhwCWYaoWK5AQDDiNf0MtCzJNohWvblHPqyNU0rva4eTioixcC7JBdXuLhZ/0M7vnTMOO0/hbi81ZkFNjzDShqh6cRMZNzOXqbzOEWtZFC2auI8Gc1w0fc5tyG33B3trqci2N46Fu95YzZF9akadxf2jXm/xCelHbIrR0jdXsTAVsY8wx0sL/MvNlZUlkGrE6DqXEr15Du32zqXkNvv6PT7PKepAud1iz42YZedWLdxSJ5yfOQNcQrxylO01YpRFQ+1cAjzx7mK45dCQRDPtnH+x3xrH3w1vKaLu7+e7pXLCPxXvd61F2/MVdZQtGS3SY4V3uGvSk1IaeVCa4Nw/wdOmkW7hPU0IP87H3afnMuLtFBJlVI1jgZ1Lnf+zgYJR6miGAwNRllm0x97GkcCVXOmnLv4Z6V+QZpFw2w/mLaR/RcJtPph3kN5GEnfu+DepqUJTwa1yjSiI2+Uy/y42zv4+3DPkFP4xe9FHiz+OVyb99sZ/IYk/trGFlDYQcdJxN/VgVPgVRyKpkZQdPARjY3ijjysr5m/mQfb7BNILGDnJGPEC6VHPaa/cxoSsOJ5SX6fu78MfCgxCbwsUFFKcUiNSTjWOOnsDQcbjG2AaMVulSOKtTMDLqUcZL1zcL6geEFTuAM60LTR0R4zdnwoTGrwDAb24ywzZqVqW82ZW9rOmW1mFN7IK2SLXTbfn5tDwTd8D3BDDDzEsHeCKAlxWkM8KslnBm6On+NGH/x3GYaomtCCi8xY6O9GYhs6s5Ezn5H7u0NOHLmdwOSV8TsnlB/gcC1qR1SsLp/M3fvHQ84euZnD55Xx++dUH+PzKKXKKRJs3hm7AAzh8993p3I2zRJNqpeUtkS/WTRcUfnHo+aGrWa/l/kHh7xZ+bePrG7mCRr6g8VZB242CtuuDbPdBrqCHL+i5VdB3o6CPdQ2xx4dvHQ/cOB7gjo/yx0e5ghN8wYlbBQ/dKHhIXI+zA3O8k9yFxdjQgqUAhgJu6MTyAUNwF3kIncOkU4zVJ8bqE2MNibHEF5COkww6AfIUhgTIhzAInbfQ2a5+W3IwhVo8AJ5Sz5RXfr3g9ZLr6dc7uao9fNUernwvX76X7ezhyntuHjp6s9fN9/rZkQdYJsj1jvK9o9yhE/yhE1z5iZsnx97BH/Gow+yEpJ85bCHb0dlN7sWrhlSdUlgnHp1SdeEROnBU0UWylG2mcsvX979+9Hozu7+XqznG1xzjKp18pZOlHDN5G19oezWPy6vg8yogo+JhPpfn4PMccJi/6YUjr9q5/Eq8e5oZs+3VJr6s4dqeawxXtosv28WZW3hzy1TKLEkUH1GjUdvJtffx7X2QPfCQGFoaG25pMf4PSjenQSpFo1SKRjI6DpT9QPi+iCbuA6Ro4kZnXrxT5IPoFSK7sPZPkfuw+tGJjqfwUXWDBqIVN6CRu1EzpMMraQ7h0WFNEIMOaEY1b0uOHCUS060dxBkIj9arfQuPhrVvS86CmKPaU+h5WhvCmKPacYyJTmxM2cEcDemmjDObS1/VvGL6auIridzmGn5zDXht2Phy2UtVV7a8tIXb4OA3OKY0s2Rq4QnVZd3l4CyB0nRh6VX1rBrFHxdar9pmtSjO6oiiksv9s3rxwEAUVbPVB2aN4pGJKLKw1qbZBPEokSjawm7ZO5skHiVD2NXM2RT5oKpOda1APkoliupV12yzy8SjNPkoXTzKIIq2vuaaXS4erJDSyJQPqnarrgfloywMSp9dKR6sIorKrjbMZosHqzFk82yOeLCGaFR1qqa3BWfXicdEhKECclcUktOFNtbeOKsG8ceFZqhIW4ic1cIRFryKrW6Z1eMBFNzxWvasEeVEYpMZrp2EcjKxqYy1t8+m4EEqsWmn6vqK2WV4kEZsKmcrjs2m40EGhkDiu1T15Oxy9FlBbKp5jZ7NRDmL2LSFrWmfXYkHq4hN264lzGajvJrYtEN13TSbgwdriE3Vr+2aXYsyJcnrUM5FuW12Pcp5KDfM5qNcQOxUtajg2aocIqe31M5uQk8iTFD8MmLDHhU+psUvHLlqe63hegZ71MXm01w+zePHM0XO5BW+sOsy81z7C+1Tqun15qu17Ho7fMT5iV3XbVxJ+/VRrqSL3SdNUri5EjdX2M8X9rOF/fL0RD1XuJMv3HmrsP1GYfv1ANu5/7sn2e6e7z7IHurldvdyhcf4wmNs4bE348xNTOdXvGZ57dDrW9n8ZvhMbyp5df3lqstVM2Y7W74fUoEekD10jCs/xjpprpxm3Q9w5Q9wZoY3M6yZmTHDzWmBbtO8hzfvuWXuvmHGeRH2cC93oJc95uIOuFh6kDswyJk9vNnDmj3QSf2O6TdNr9m+mvJKytWUabP9qvYtI7G5/C1o3paZrNUXnU/p5QnXmcy1fOZGPrNqllAt2xAhiPWsacr6VPKzyRfl/5lMCoNyIjQNSWnC/+/iFtZq8MVftEId+CO1ZXs3Et+oyK5LJ95IU4H8RrqmbqX6jcyOZXBwY2NhZ5H6R8uNyHla4PjzLltMS/Mudzjv3uZdNEfMS/MuS/Mu95ebpXmXpXmXqPCleZeleRfl71d23uWl+fMutDdmDuZpenjRORjfeyq3/xc+B2P+sPIjrnbVnLd+SHM7Ix/I3M4D7WPWedsjFYs//uTxDdz7JklxpoKY1WipwpkgJgelNUhrkSikdUi5SOuR8pDykQqQNiAVIhUhbUQSp5Lk+ZpAb/0+ab6G2YxhxUglin3MjGRBsiLZkMqQ7EjlSBVIDqRKpCqkalI2EzI1SOLq3a0obUPaLtoPxUszdSiTIDRgiGiYa0LagbQTqVm0ISK1ISkzBUw7HkbePd2Nhx1Ie5DQKs/sRakTSVxP3IWSuO54H0r4w9dMN1JkBfIBPDyIFFmL3IOHh5DuZNhmcAWvtO74CEriAuejWM3eOxiW0aIsrTbe5vG5vKO0u1feS7um3+kNuAtoN5o1e/v89OlenD6SvQNBxu0cxlkm0beXcQdG/L6AuwbnupqYXrz6MSQn0qJ2Z6ZPug9oahb0w+5AwDngnmdvZmhMxo00DHRXs+hkmHBVceClO5lFPTeP+2+OBG4GT3Ijp/iRU+zQaa7oNJc1xmeNsVljNx98SLRQNaHlL6RqRcsfOqL1ql2yXomGOXSWTKNLptEl0+iSaXTJNPqLMY2WEBv2kb8KptHu16uuefjqDjYfP78Y++ibUir1nLmDN3fcMu+/YcZLs4eOct1H2d4+rhu+SQa47gHOPMibB1nzoHjaXxaaf5721M7VEXsqyGF76h41HPxodWFXtprXG5FXaIGX3tKOKcXSW9pLb2kvLMHSW9pLb2nHz+vSW9pLb2kTvzRvaY+lSz+g90u+D/fCPL7fV7fHdt5n4r9E+3BXxHv/W7R9/Tzf/34sTGj4i7cP99L730v7cC/tw730AvjSC+DyC+DRIwhFcd6ikb4YxhGqYNSXR5yFP9FfLZFBgGrBAEYbFUouCI1aBkTPV1BIY6wqHh133jB/3plqX9r6mKEhDHG0ohKrjhm+JEVihOZdvYE4Uj+uoXV3WKikP0tEn00b5p+96LBZGyLi1x8or/Nq6HxDcFkknDa+NG9pgh2X5ixyp4LpkbCYJQ7zlavYHOpj7ltCSB93cBodJzFE3jVO0qKhyQtCo5SYBS0Q79CmcUOIDBnEhRnGkAHUvBRUq+m0Ad24KaSbSiTi/AWj1J6QMWT6ArT9LyuGJKjxzUaCFv9jB/EwpE5YT1iIgAZ6WbH94GBYNb8U6fdTipgzMxatneV3upN3NjwsXPBErxAXT90ppTsuWVqY0vy8isP+zHZxODeWH34Rpd5Puyn3KSf+1mkVZbaUbzZbKgAOQOVYWnjKemQ0SOGcYxU1tyV8qnKW1Ww2b6ZsIttFtgCbTdEnez3DnmAVdfsclEyIHfaiMo+LA366F6gFcvokDnxzY/u3iKkuqInyVVpFbGn3E0/CvT+/Hst8RdV+RSO+3SK9yaKTXvQQdLRnwBMMXCGZv0BvVW8AG1L4R4SNW/DFulMjzNax5X101Bg67I2xAyVwxt/B/wTB5u+Dz7UHXux/YfjVplfauII6vqBO8o3+iAPu29ihMw9glhgkLOjc2nB11Yu/sitWN1VSUhWu7jnlnu0Vf46X6nIHglAQar/0EgvEhT9qbGM4nehfEe5g/PgmkvR73m5a/g1hwdTn9A14nbQ7MDhm8lBe/wk3ddo/Oqfbvh7/BZ3FanNUmqUfHYY051ZRXYNuaoTxuzC1QWeACv9MLj2XTHX5g04vtbultL4DGoqq9EoqcxTLJ77+I74N9BDSR7G+Tfvxl5ul3/H9GPrWIj2KJL6OJL6xdBjpPEbXOEc8p6Q3mPAVoqIE5nMoiz8UrBFf8tGKTUzQ+Ib7GEHtGx4R1AFnUCCDXvzV31PSO0X4OlEggYhRVCQN5eEwDeCNxQUDE8T08sxJzXTGikn1TOryC/rH9ZP66dT0J02fMV0s41IpPpViUykIYlds51Jr+dRaNrV2JnM1m1PGZdr5TPukBjWP/Blq/YuN7EY/lzfC541w1AM89cBF7UXtuzOZ69Donh+haSoPQy5q0eyejyOD1eum8p9qfbZ1liCXFYmEegf1uYGnB6QW9YNGdm/nd3d+fyfIXP4+HnjNPn7Nvovq6azVojJUz2UV8lmFrPiZWb5yqo9dXsQtL+KXQ4IJy7Ze7pzJynlK/6z+on4mh3oxfarruZUvrHzq6LNHL5IQwq6pfq2OW7OVy9rGZ21js7aJfk3XgtyaFi6rlc9qZbNaRb9mLmsXn7WLzdolHnZxWfv4rH1s1j4l/en1G2YJ9cqtIl2sny7YCEO4wSn19ObSq+qrrddW4+R5L7vp2JRhWhrivVwGATs5qoanaljxM6vHBJZBxsXci/QW0ttEjF88wgmNON7vZBHLVkx6udT1fOp6NnW9crvFm2vlUm18qo1NtYmHBS8GXra9HLjieMnx3PgL49yKsqud3ArH19O/3vmH6V878PqBr+W8nsOtaOJSd/CpO9jwJ4Am1G/oV9fmEd/IS6y1qb9hVQF/c2VdUVOK+tspmqZ0/bdXqIBjxn7YWMWx35d+ycZ+MedqFj1XO3/0t8i4UbfoqEdzh3GjXlxyHn/cqFkwbmwY19KGO4wbjfPGjSY6IXaUcZeRo+6OI0fdgpFjY8zIMfGlpAUjR/2HMHI0xI7ppNHZoi0j5R5GjqmLhi6775FjPYwXyZA6Yn6F8SIcK34knSa64aN02c2Q3eXSaIrOHDCOw+j4HkaaplDCgpFmw/saaWa955HmykVrc9UHMtLM/lBHmqvlkWZpeNSCe1ZQkUEj1TnoHPT4NlOdzr4+D7OZavIzg06aGkummjxMIEjh3gBUFTWWL53ZKJ0IPrVe5/BmatAfCLh9kuv0+MaSqFZn5CzmY2jhfATpHEn8XMebzMfxqp9A+hQOJaJGlcwkHIytGBj2xhlQPj5/QNkNn4UDyu55H8mCW42jSmwi80aVzGcwH4/hZUvijQt3OY/DSBNXolLzxobizICghgGgoAEqE7TIduYJTPCzSE8iXUR6CulppGdwbJYYGZsxvy6uI8QB2inmcxgDZ1qY55CeR/o80gtigDI+SyRiDclS3U2ECW9t4Ln7HKDt4lJb+NQWNrVFHKAVc5klfGbJpEYMrOFSt/KpW9nUrTBQuejnskr4rBLJbPwhDt7w7omDN7Zr33d3fX8XHHL53Tzwmm5+Tfcvfvx2gMs6yGcdZLMOLjZ+sz83dDX9OR+O4cxXl18Nvtb41bFredcC3yi8bv9GCbtnH7v/ELcHDWisc4A7PMAOetnhIDcYZEfHZwniYZW49nHzTvJ/65Avf3UdSbxBJtYtU7+RqgL+pqNetUOn/o5Os8Ok/06SCtgVPf+oDPleM0jvHYZU4t6Fj8GgKyra/6Y1M9FfQ0NK7oIrIr7zB4Ihdfyv9PnD2Mj6j3FtMGp+dkjJF62OXvUw38A3b544asAWdc35qyjiX0f7c7qO7ud0Hf0HfR3aQBtCOHgz0qZnjeM6j/iO4GMqOolOBk6hU4GX0WnA6XQG8HJ6BXAmnYXrcehVwNn0auAceg2+f0VTC1biYGgBvQG4MKR5TDWuh3aUFjdvRSFdSP/SxtghYVRrMoTUkXUw8de6zFvNEXdly7wnwUhvChlPEMyP6M1TK+LFp4vFdST3d+V7WGtyF7XGFDLRJXTpR8molWcJMW8mmRf0GtGhFnmdhlUanouy7W7vLc1/yw9C7VFpltH2e1zFEX1V811XqWTHTyXOKo7v0eXi3frWHe9WxS/sbjnoyvd8t6ru+W5F34/qD/B+RL9ldu/3g5xUn38i3pqXO3y/VEV8o1cZRa/pCW6Pkuui5IaIPDBPtR9P/BX8nn4f50rv2YXfjZPfedsirTAaWx15y8npHRl0xq4eEpfciEuPcN3N2ErU32pyh3uDgVzqBFqIa3ILSzZuK8ody5SCvJ55AQz+tPuYrtU/QDX7iozMDzGxP0blRYPJCKTXI5hw2zvf6HCfmxHSRn2M2+Uf8HnG3HRvkMFN9sRX2X6EJ1aFXyYby4ibX3wBTdB07O7sEnQB16B72M3oVPL6pbFfkv3pKsUFUmPa0WB/sSPuW3C4UmusNneH3z8AKrW0OZq0EZxZ3Byu3R8sqq2O7BtXWblwyzhz9EZxUeu87vgenLimS1zJJS77EheA4dqvscHFWki85VWMe2DU62TkoG2Muz/AuGpo9wjcWCeosAXO4ZFq78kTNZBJUYYYHrrGUURG7c8Wfw0WKvviGqw8QlmDlRRZg0UTkZ7rAnk++V5WYa1lRAW7t59xu+MtxrpJypcDpT9tn/R57uBU5+Xlk7bJwIWKi/YLNUqANH/0JMS+jU+huExrbJmos1uH5+0qN6bPPmRGXX5MB3UZPBWUlnf97S9Bmf8cW+ErpLwA7fYnsTzPEkpRLHJR6juOUGM61whmvmj9vexsJ25H91OkyIyfcTTgZuBh8gWZevQUN6r7D6Q5VXi66T+RxG3s/hvpf5B+pgpPSxGkPIEl6F3u473OkeNR+9rhfJSgGhZUxwXVoKDqE1SjgupUUZKg9tD9gnrk5AlGh+drMZ56hPELeqyW3v4+wQAtuJd2Bp1CkvSGp1hhEEB6/UICBoa3AU0VT3Z5aIHs8weSiHlL7cSqFxKiap35vvxVHBjQiG9aJm4h9dOJKbNEmTrpLaSJvnd0hEZ/tuqWOv2GOp3N2Huz68DNg4dvHjnGHXTyB51sZx+X0cepXbzaxapdN+kBnvbdooM36CBHn+DpEyx9YiZpOZ+UwyWt5ZPWTlTMGFPO5zxxmjOu443rJmzTSRmfPvTxQ+zKCi7JweOnZqLiTVPi+SI2o+RV9dUd4vtjphreVHPLVH/DVH+tljM18aammaSU8wfZTPurgdcqvhp6JcQlNfBJDbeSdt1I2nXdwiW18UltM1I6pa+mX+3+6upXVnOmrbxp6y1Tww1Tw7U9nGkHb9oxYzCdN7Jpm17uvJp55fBLhzlDFW+oumXYfsOw/doyzlDPG+qnU9Ons7KnE5KnTYnTCemz6caU5bME0IRjNiMpY8VkC0uVzxIgTasTzu2fVYP0Y5C6Z7UgzUIVJs4SRHI3OavHYwOhWT7ZPWuU5DWlrHm7dGAiNOmTLbMJKCcSmhQ2tXM2CQ+SCc2KyeBsiiTnWK5ukuRUQpMx2TO7DOU0SU5HOQPl/bPLUV6BctdsJspZhGbtlHp2JcqrCE3qZPpsNsgTNbOrCWPqpxM/nsgufxgX3UlvZ3aTNHku8S2CMLpxcZbMQ+SEdTplxfmHb6VsuJGygUsp4lOKbqWU3Egp4VLMfIp5ovrHuuTJTawuBz7TxsRPZ308S+qarm54pfSWddcN6y7O2spbW29Z996w7uWsXby1C4K5tH08sHE/b9w/0TBtSj4XmLSdO3m+eKJ+RmM8l3em5WzLRAuIrImaSudMeVP7ONPGy1bOVHzZy5mqOE01r6lmNdUzmoRzDWfazrZNtM1oDOeyJm2cJpPXZN7S5NzQ5Fx0TeU/5blMPuW9XMatKeU0Zl5jZjXmGY3+kV0f2XUucGb32d0Tu6c1xonGaUPGxQTWsB4+v6CSvK/s/6UmcYbUnVOd2TCRN6NPOjv+hPOS6tK6S7WXnC+qJo9w+vW8fv1E7gypPbvxFpl2g0xj0/fc7Oy+eeDQTXw17Rh/4Bi+EJvu5Mg+nuxjyb6brn7eNXzLFbjhCnCuUd41yrpGoxLgyAyezGDDn3dnNSroVUjdRN5EHr4khiaZj+xJ3ZNBcBnknpXqGLuWsp/WmqRf3f20GohJ7ZEfj5PRdq3oabwhJWc0SasX3W1JI07A3CkdpVS0ltbddbel950bcYpNfQ/p6GnDonsSaWLOU97ZCka9dzN/sd0AQRsvqGgTIAGQCEgCJANSAKmAZYA0QDogA7AcsAKQCcgCrASsAmQDVgNyAGsAawEUYB0gF7AekAfIBxQANgAKAUWAjYBNgM2AYkAJoBRgBlgAVoANUAawA8oBFQAHoBJQBagGbAHUALYCtgG2A2oBdYB6QAOgEdAE2AHYCWgG7AK0AFoBbYB2wG5AB2APYC+gE9AF2AfYD+gGHAAcBPQADgEOA44AjgJ6AccATkAfwAWgAW5AP2AAMAjwAIYAxwFewDDAB/ADRgAPABhAABAEjAJOAE4CTgFOA8YADwJCgHHAQ4CHAROAM4CPAH4NcBbwUcDHAI8AzgEeBXwc8AnAecAnAZ8CfBowCbgA+AzgMcDjgCcAnwU8CbgIeArwNOAZwLOAS4BfB3wOMAV4DvA84POAFwAvAr4A+CLgMuAK4EuALwNeArwM+A3AVwBXAV8F/CbgtwCvAF4F/DbgdwCvAb4G+F3A7wFeB3wd8PuAPwBcA3wD8Abgm4BvAf4Q8G3AdwDXAd8FfA/wR4DvA34A+CHgjwEsgAPcAPwIwANuAv4EcAswDfhTgAD4f4A/A8wA/hzwF4AfA/4S8BPAXwH+GvAm4G8Afwv4O8BtwN8D/gHwj4B/Avwz4F8As4C3AP8K+CngbcA7gH8D/DvgXcB/AOYA/wn4L8B/A/4H8LMLqknQIERWiUyKrL6g2osLY+P2FfOXSozr7zGe4e69KVxbA9Au2ocZIYYuOq2F+5FBDH1MjAV7o0GMmPws3PMMYhhjYqjjxDDFxNDEiZFwKQE4cUwqXdJd4yfHxNDGiZFy15KlyrutxeQuGGWpi+yBt6ilMuF9np/owdwsA6Q9hu0qHfdcAzcjRIrucsAKUcoEZInSSsAqUcoGrFb8ckRpDWCtKFGAdaKUq0jrFSkPkC9KBYANolQY0otuEWCjKG0CbBalYkAJoFTcsS1JzLcZYBFDrQCbKJUB7KJUDqgQJQegUpSqANWitAVQI0pbAdtEaTugVpTqAPWi1ABoFKUmwA5R2gloFqVdgBZRagW0iVK7kspupbQdgD2AvWLuk0HqHE8Jro26X6lKe0kJJYUwRtek6qV98/Z/U57J8dTod4ojFvLQvIVE43hv94eWnSCYoWBR5Azw7Zas1CAdiFgo4OhgXIvypphzewCH7s1aDTEPx6R/5K4zCHHnAuJarH8P0jsawjL2Rmz1cHQsZle4L4CPM1hCRPvNr42+91Ebrg+8NszvqTbKPux8iXME2vM/idYlIC4ds19c1NKnIeU2DClLxfIIZiWUMOot5CFl2RWk5V74Pq64Y1zUXIO4Y1yauGNc2kNp8o5xIEV2jCvshwTkHwS648Zu4mu74u5u+I3IoO7FoI7FYNfJYL/K4EPJ4DPH4CQng08Zg1NQDM5FMnhjGJxtYnBwzmBZGSwmg/0wg4VicOaXwQph8FlnKKR14nWR8C1kBq2GDD7LDG60x+B+kEwhErZPZiMS3lVmMxLu+chgQ2ZKkbCZMDjzxFiRcO6PKUPCeSUGN0JksJ6ZbyPhnBCDr3EzWJdMNRLO2jA1SDhnw+Amfsx2pFoknK9h6pFwtobBF6iZJqQdSDuRmpF2IbUgtSK1IbUj7UbqQNqDhCvGmE6kLqR9SPuRupEOIB1E6kE6hHQY6QjSUaRepGNITqQ+JFzuy9BIbqR+pAGkQSQP0hDScSQv0jCSDwl//okZQXoAiUEKIKGSy4winUD6DtJJpFNIp5Hw+WAeRAohjSM9hPQw0gTSGaSPIP0a0lmkjyJ9DOkRpHNIjyJ9HOkTSOeR0KbLXEf6LtKnkD6NNIl0Ael7SH+E9H2kzyA9hvQ40g+QnkD6LBLavJmLSE8hPY30DBLajZlLSL+O9DmkKaQfIj2H9DzS55FeQHoRSTSffxHpMtIVpC8h4ViDeQnpZaTfQPrK/2/vToMaOdM7gKt1NpKQEPeNuBGaWQ94wMzYY8NwDMxwn8N9SQKBQEIHh8Qhb1wpJoWz41Q+2JVs1biyqfJ+G+f0bPbw5KiKq1K1aEOyQOJknWSTzbWRkk3izd1Pt+i/YBgvsddxpUoe1b/7p26J7lZL1tuv+mmKhxRvU/wSxS9T/ArFr1J8k+LXKPYpfp3iHYpHFF+h+A2Kr1J8jeLrFN+geJfiMcVvUvwWxW9T/A5FiOJbFL9PcUDxBxR/SPFtikOKI4pjij+i+GOK9yn+hOJPKb5D8QHFn1H8OcVfUHyX4i8p/oriexR/TfE3FH9L8XcUf0/xfYp/oAhTRCj+keKfKH5A8c8U/0LxrxQfUvyQ4t8o/p3iPyj+k+K/KP6bQsIfUKeQUsgo5BQKiv9NEUv3FsU5dSv9JdesV2zPXrlSffnqs7ZZLmrqLtdds1Vdrqmtrp65euVZS82V6k+vuqV7m4JqW7p3KMTilv6SWmtVXV1tlfWypea5ustXZ20zl+ueq667XFNdZ6uyXp25dsX63I+zBObpwpf+iif6/aqvPtnvV1VbxFfH9F87Z/anXV+qqpa7v6buas3nqq+e6jf8mDU1T/cl+j+FK0XxS/yRV4oySXGRKHeQW9yPUWLT/TLF5ynOFNfk+8SpwqYp/yL9XuIlnNw2ejI6iYnv/HLP01gv/+f5/Y7GTl+uyb140rt10Ys1uR20XCn4yS5/VSb3CgV9K3HTj57ddgovhY9ilWLtZGc/c4kl9zrFBoWfIkAdV/Rt5anVRL8ojcb3adaaFKGaaMendpGlYnNY0swXAaV8vfH/TcnMsFRSPnDpgZ97dm740CQM32kThu/aheF+93B0ZGQ2OmJZio4srwkjVBSCW2gRjdJ2oEM6BNwViiQIoBoJIpzSDcAv5UtWCGiWdQHdQv0KAaMyK2CTuYAVoWKCgE2hvoWAFnk30COUt4g+m9wCWOUuYEXuBwLyJgWWTah7IaBLqHshYFgxA8wqHMCSYhVYU9QrRTQobwN3lP3AgHICmFTagQWlB/Aqt4Bt5S2ViFZVD9CrGgXGVFbApnICLtUG4Fe1s3hN2UFgiJ0AJtk5YJ5dAdxsANhkWxJE3EroBnoSRoDRBAtgTVgClhPWgY2ERrWIJnU30KMeBcbUNmBO7QY86m1gR92lwf6mGQFGNVbApnEBK5oAsKlp0WLltD1Ar3YMGNfOAfNaN+DRbgHb2rZEEbcT+4GBxClgOtEBLCWuAeuJjTpsHV0n0KUbAUZ1VsCmcwErugCwqWvRY+X0vUCffhyY0M8Ddr0H8Oq3gR19WxJWLqkfGEiaAqaTFgFH0iqwlnTTIKLR0Al0GYaBEYMFsBqcgMvgBwKG5mQRLcndQE/yKDCW7ACWkreA7eTWFBFtKf3AQIodWEjxA4GUO6ki2lPHgPHUecCe6gG8qVvAdmpbGjZi2gAwmDYNzKS5AU/aNrCTdjtdxJ30UWAsfQ6YT/cA3vQdoD6jOwObKmMMGM+YB+wZXsCXUZ8poiGzHejIvAsMZ84ClsxlwJnpBwKZLVnYLbN6gb6scWAiax6wZ3kBX1Z9NhYnux3oyL4LDGdbAGu2E3BlB4DN7Fs5Ilpz+oD+nAlgMscOLOT4gNWc+lwsTu4doD13EBjKnQZmcpeA5dx1YCO3MU9EU14X0J03AozmWQFb3grgztsEtvJa87GT5/cB/fkTwGS+HVjI9wK+/B2gvuB2AXa+glFgrGAOmC/wAN6CbWCn4LYRT2AcAAaNU8C0cRFwGFeBNWNDoYibhe1AR+EQcLfQCtgKXcBKYQDYLLxVhJe+qBfoKxoHJormAXuRB/AWbQM7RW3FIm4XDwCDxVPAdPEi4CheA9aLG0vw0pd0AJ0l/cBAyTgwUWID5kqcgKtkHdgoaSjFdittBdpKe4De0lFgrNQCWEuXAWfpBuAvvVkmorHsDtBe1gf0l40B42VWwFbmAJbKfMBqWWM5Nkh5O9BRPgTcLZ8FLOXLgLN8A/CXN1WIaK7oArorRoDRCgtgrXACrgo/EKhoMYm4ZeoBek1jwLhpHrCbPIDXtA3smFor8ZJU9gJ9lWPAeKUNmKt0ASuVfiBQ2WTGmpo7gS7zXWDYPAPMmh1RcO2TJfMqsGauvySi4dJt4M6l/kviE3D5QMG3Wx6eru3/8Ina/o97Hp+p7R85v7Z/5Cm1/SMXqO0fuWBt/8gFa/tHYmr7R2Jr+0cuXNs/cuHa/pEL1/aPfOLa/l9Whq4MCtXuj1Dc/wMU949Qcf8vR4v7R6i4f+ikuH+EivuHqpqF4v50YcgXQifF/SNU3P/taHH/CF/c/3G0uH+EL+7/OFrcP5IcFV/cP0LF/R9Fi/tH0oXnyIjiehfzXrS4fyS2uH+EivuHro4I1f0jVN3/7Vyhun9EqO5/9JI3cm51/7Ry6VFlTei5W2EZN/pBZTW3DWu2pWEFJ27NzS+EbnSEVQRWYr7+6PlwAo1Tdf+3U8KJNK6jsv3vpYf1hCSJuTb03HTYQEimKREq6M/tlSl0T6rEfOORJZxG4+n8k3eGMwiZEvNLjzXhLBrPpoL+76nDOYRcifn5R7fDeTSeL4wX0DgV93/UEi6kcSru/6gpXEzjJRJzC/PYEy4llFFZ/6MXGiImTmHJSTyQRy5Jzpb1D03Mhp5e1v/oVFn/ULSs/3so6x96oqx/6HLj4zNl/UNiWf/Qjy7rf0Rl/R8NffX6Y5T1P4op6x86KesfiinrH3qirH+o5s57Z8v6h2LK+ocuVNafnuVsWf9QTFn/0FPL+r9xwbL+b37ssv7U8/f5YXZYKznSmka0sqO6BC6PVQouTxWioeoC/K83N2X0600LsyWJLZjgjan0v4Df1Uie/tuNpz4aRRY+4tH8r08YC7c7Ss75b/NMqZstqTemerw35szhJ3quzz1f+Wz5G/wecosvSbIqcSfFls847wypU+soLs05pXPOn++JwoPnV7k/W0Dnqc/35N+96BaKmc+i+gRT2Y+cmvAJnlm9GXPOykfOqXliasy5zpYz19Pckv+IZYh97JOlFC/6usb8qua8/cik6/TL13y+y+4a6vuoOzl7as7unffN8OdMUVmPNZ+nqvrZZ9qdjmdmHM6ZZ5am7cvPNLhcbufqtIM/G4hqs/mr1i1zl50u67Lx5HnW1tZOn4FF1fyuXampulpde6Wq+sqcsDBsPV9axZ817PS5jXesG0a7x9jp9BqFv2G1GP05xkana4M6Yox9Vi5opn6nscGyZF/2a43iA68bhfOYVHypl+tGf6ax200F5pqXvVY3PeTk4aYkoafjRYqXKOop+JN0+B6MLuakkwOn+vwCRStzqgeDCtEdKxf47WRSHMsGOrqEXpI+miBvaui9w19Wz0MfezHdDt+URuMG92p6phi+CgmrCza+r9G96t7z39vc2wxpcg80uV/0/GL1l55/88aXboQKqg4KqkKaqmBT9DSD+yX38vfygzfflye8enK6QIJhL3c/vTuU0HNANzqzQJWw2x/0B/3vs9p7yj3lLv/vu3ROy/3yEJt9wGbvs9nRc1yaQ2zLAduyz7Zwc++p7z97T7+n39U/OXfiq5Z7mj3NroYb3XXfU++pd9WnR/d1phBbecBW7rOVPM0h9tIBe2mfvXTmMduvz4b0hQ+KQvqSEFt6wJbus6V0v/eedk+7q31fn3p/OKQvONAX7MrP/o2KEGs6YE37rOmcNdDdY/fYXf4ff4aYSeGmX+y4qWaXm6+eSB/AbvrNlalD2Bvo3XWspBMEa68ey/0O+8yxzGV3HSt9bgcHYad4QezH+qHYYcb3rvGv/Z6UChN6fDPRAofHybPO5Vmf221d9n7O5vP6uJ3SzVfZoTqFxykdTovPYeX2+Ranb9ki1DJsFTvd+HPPpHNeoSOsie5vpmjh9zCqtej+kPwVmvyT/MzrlmPp9LT7G9Joj94xM3vMzAm9eV+n+Dn+zgX312hJGcexwje96Kvmu+yOFfwpbseMhe89O2Zsx6zN53BMzy173Y/pHn7maXe3+D7hyytOiF2KYnVFofePfyeovM5F6/Kizz3Fd1mKb6dXKb5A8RrFz1D8NAV/lT++3DtfUZGv2vN7J311wtuHP3GQL1vEl9pkX1jit+OL7u9J6TOOe1/9RLNEwn1DYehyYEzqviQl9nYoMe5/3FtYqmS0h2zb/mdxO2Rz909uh2zD/hO3Dw9V2dzXNeYmE5uHrGFXSm+Q+hDbcBAz+6FEE/QGvdy3uCOFNyg/VCQHB18Z51pzqc3NzOkB145QtjQzPxAGQaoxr/KZg9QpyA3vm4Th623C8IFdGD5MEIbvRKe/G53+u9Hp+3enoyMzi9ERx6owEqb+Sr6vUECj0L8poEs6DIxILYCVa2iLcEn9QEDaLBPRIusGemSjwJjQVygg2lcoYEXmBwIy/rp6ApqFvsLoswl9hQKifYXRZZMvA075OrAhv6nAmiragQ7FIDCkmAKmFQvAosIL+BTbwI6iTSnitrIP6FeOAxPKOWBeuQK4lQFgU9mswkZUdQHdqmFgROUAllSrwJpqG9hR3WJFtLI9QC87CoyxNmCOdQErrB8IsE0JeEkSOoDOhLvAcMIsYElwASsJAWAzoUUt4pa6F+hTTwCTaifgUvuBgLpZg02l6QZ6NKPAmMYGzGlWALdmE9jS3NJiU2l7gT7tODChtQMLWi/g09YnimhIbAc6EoeAu4mzgCVxGXAm+oFAYrMOK6frBnp0o8CYzgbM6dyAR7cFbOta9SLa9H1Av34CmNTbgQW9F/Dp65Owckl3gPakQWAoaQaYTVoGnEkbgD+pyYAdydAFdBtGgFGDFbAZXMCKIQBsGtqTsa2Tx4GJ5HnAnuwFfMltKSJup4wAoymLgCNlE9hKaU3FRkztA/pTx4GJVDuwkOoDVlMb0kTcTOsF+tImgMm0BWAxLQBspt1Kxz6a3gf0p08CU+kuYCV9E9hKb83AKmT0AwMZU8B0hgNYylgHNjIaM0U0ZXYCXZkjwGimDZjLdAOezC1gO7M1C4uT1Q8MZE0B01kOYClrHdjIasrGjpTdBXRnjwJj2XPAfLYH8GZvAzvZbTnYKXIGgMGcKWA6ZxFw5KwCazkNuXiBczuAzty7wHDuLGDJdQKuXD8QyG3OE9GS1wP05o0B43nzgD3PA3jztoGdvLZ8rFx+PzCQPwlM5S8Ai/kBYDP/VgF2voI+oL9gApgsWAAWC3zAakG9UUSD8Q7QbhwEhozTwIzRASwZ14B1Y3Mhtk5hN9BTOAqMFc4B84VuwFO4BWwXthZhTyzqA/qLJoDJIjuwUOQDVovqi7FyxXeA9uIh4G7xLGApXgKWi72Ar3gL2C5uKRFxq6QL6C65CwyXTAMzJfOAvWQFcJcEgM2SplK8f0o7ga7SYWCkdAaYLV0EHKUewFu6CWyVNpfh9SlrBzrKBoDBslnAIvQVRl/tsjVgXegrjH7ulHcCXeXDwEi5BbCWOwFXuR8ICH2F0dUW+gqjW1ToK4x+ilXYgLmKFcBdsQlsVbSasO+Y+oB+0wQwKfQVRl8SkxvwmDaBLVNLJV7tym6gp3IEGK20ANbK5Si4VoSzch3YqLxpFtFobgc6zIPAkHkKmDYvAItmr1n8O1wGFUcKbVB2pEg8CaWOGjaqk1BrgwmHav1u6WuKe5f2LoUlGiaHj+DNI415V3qoztgt27u8n3kjlHmDki8KssscqfPv993vez35taGfHdpX53M3uvP6LnOozt4tO1Bnv1H9xmxIXXSgLqIJiTETrr4pD6lLD9SlT5vZyE0wpOzrakO62vvTwvD1KmH4gOGGD06wIgzfivqtqB+Suduu4pDVfkHzU5r7zeIBG+52mJi8O/Bazb2xvbGwRMfk8xFsPtI8E7PCdaHMOkr1tQP1NVqq52hx+Yncts0aof5LLsVxzSh1ZXIZs1ZVWKsLPvRI3fJj2YQF3IS0jP3kxlBy4+uF0eEKN3xAeNDDxVuMcPdbhIdRPGwQhu9E/U7U75K52y57skVbQ2zeAZu3z98OE3S7afd893L3cmljZvERbDiSm4LJh7KkYO0rN/YN10KGa5Sy6wey60HDkaw0aIhO5DZFMv/TXC7FcTn/K10uabaUYO2BLOW1htc8IVnOgSznwg89kk3GPP4mHn8kU8ZMaHojNSTLP5DlP21mEzdBrd1X1YVUdbsrwvB+Aze8T+C2MRc9wt0PCA+ieMsQHUb9MOqHZO4WTDtk1N9mDN9iDPdLQ0zmAZO5z98i8qsM93X2JCIOJlH1YlAeMTJMOh3IECIilzLcd1YxlBIlva/lyqAsJmSKoPSQVQdVEbmC4T4LTyKiS2S4dsdJRHJfYqrDkpOI1EsrGK4dIEYvw3+oxI9y8P8nih/liB/lCMePcvArFz/KET/KEY4f5eAXJ36UI36UIxw/ysHvVfGjHPGjHP8HRzki8lMNlUgvE2+4xBsu8YZLON5w4Vcu3nCJN1zC8YYLvzjxhku84RKON1wI8YZLvOHCL9tn13CJ97DEGyrxhgoh3lCJN1T493a8oRJvqITjDRX+IyDeUIk3VMLxhgr/uRNvqHymPSz9DMN9riAjC9Jz7oo3Z+LNmXhzJhxvzvArF2/OxJsz4Xhzhl+ceHMm3pwJx5szhHhzJt6c4ZftM2zO5DGtTFiCjLxYwI8jI7eZmwzDfQ9FRlqknXxrBxmZkGYz3P/HxaiVMKqg8mX2FTbIfkciD8pfVr6iDPL/PHTlqJ+vbtBLHuvTGkyyx2UMl/8DlqqJCg=="))))