{% set statuses = ['placed', 'shipped', 'completed', 'returned', 'return_pending] %}

with orders as (
    select *
		, EXTRACT(MONTH FROM order_date) AS month
	from {{ ref('orders') }}
)
, pivot_status AS (
	select
        month
        {% for status in statuses -%}
        , sum(case when status = '{{ status }}' then amount else 0 end) as {{ status }}
        {% endfor -%}
    from orders
    group by month
)
SELECT *
FROM pivot_status
