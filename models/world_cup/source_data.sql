{{ config(materialized='table') }}


with source_data as (
    select *
    from {{ source('world_cup','world_cup') }}
)


select *
from source_data