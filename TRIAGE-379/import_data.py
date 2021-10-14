import scanpy, os

resource_dir = os.getenv('MOUNT_PATH')

# Import PBMC matrix into AnnData object
in_file_dir = "filtered_feature_bc_matrix"
adata = scanpy.read_10x_mtx(
    f'{resource_dir}/{in_file_dir}',
    gex_only = False,
)

# Write only Antibody Capture to File
out_file = '1k_PBMCs_TotalSeq_B_3p_filtered_AB_only.h5ad'
is_AB = adata.var['feature_types'] == 'Antibody Capture'
adata[:, is_AB].write_h5ad(f'{resource_dir}/{out_file}')