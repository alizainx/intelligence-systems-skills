// CUDA C++ / OpenCL Padded Shared-Memory Transpose avoiding 32-Bank Conflicts:
// Adding +1 padding column (__shared__ float tile[32][33]) shifts each row by 1 bank (4 bytes),
// making both row-wise coalesced global loads and column-wise shared-memory reads 100% bank-conflict-free!
#define TILE_DIM 32
// __shared__ float tile[TILE_DIM][TILE_DIM + 1];
