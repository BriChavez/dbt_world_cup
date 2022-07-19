
select 
    Player,
    Position,
    Caps
from 
    {{ ref('players') }}
where 
    Caps is not null
order by 
    Caps desc
