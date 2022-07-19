with player_caps as (
    select 
        Player,
        Position,
        Caps,
        Club
    from 
        {{ ref('players') }}
    where 
        Caps not like '%0%' and Caps not like 'n/a'
    order by 
        Caps desc
)


select * from player_caps