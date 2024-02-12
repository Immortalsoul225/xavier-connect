import React from 'react'
import './Popular.css'
import data_product from '../Ascets/data'
import Item from '../Item/Item'

const Popular = () => {
  return (
    <div className='popular' id='canteen'>
      <h1>SUPER DELICIOUS DEALS</h1>
      <hr />
      <div className="popular-item">
        {data_product.map((item)=>{
            return <Item id={item.id} 
            name={item.name} 
            image={item.image} 
            new_price={item.new_price} 
            old_price={item.old_price}/>
        })}
      </div>
    </div>
  )
}

export default Popular
