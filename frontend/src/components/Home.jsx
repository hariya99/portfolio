import React from 'react'
// import {MdOutlineKeyboardDoubleArrowRight} from 'react-icons/md'
// import { Link } from 'react-scroll';

import image from '../assets/myImage.JPG'
// import GetHome from '../Utils'

const Home = ({firstName, lastName, intro}) => {
    // make REST API call to get the data from the backend
    // const data = GetHome("/home")
    return (
        <div name= 'Home' className='h-screen w-full bg-black'>
            <div className='max-w-screen-lg mx-auto flex flex-col items-center justify-center h-full
            px-4 md:flex-row text-white'>
                <div className=' flex flex-col justify-center h-full'>
                    <p className=' text-gray-500 py-4'>
                        Hi, I am
                    </p>
                    <h2 className='text-4xl sm:text-7xl font-bold'>
                        {firstName + " " + lastName}
                    </h2>
                    <p className=' text-gray-500 py-4 text-justify'>
                        {intro}
                    </p>
                    {/* <div>
                        <Link to="Portfolio" smooth duration={500} className=' group text-white w-fit px-6 py-3 my-2 flex items-center 
                        rounded-md bg-gradient-to-r from-cyan-400 to-blue-500 cursor-pointer'>
                            Portfolio
                            <span className='group-hover:rotate-90 duration-300'>
                                <MdOutlineKeyboardDoubleArrowRight size={20} className='ml-1'/>
                            </span>
                            
                        </Link>
                        
                        
                    </div> */}
                </div>
                <div>
                    <img src={image} alt="My profile pic" className='rounded-2xl mx-auto w-1/3 md:w-2/3' />
                </div>
            </div>
        </div>
    )
}

export default Home