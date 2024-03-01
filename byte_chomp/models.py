from pydantic import BaseModel


class CacheConfig(BaseModel):
    n_sets: int
    b_size: int
    assoc: int
    pol: str
    output_flag: int
    filename: str
