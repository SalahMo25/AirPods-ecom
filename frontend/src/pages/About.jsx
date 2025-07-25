import React from 'react'

const About = () => {
  return (
    <section>
        <div className='about'>
            <div className='about-content'>
                <h1 className='text-center text-white text-4xl uppercase'>Hearly</h1>
                <div className="underline"></div>
                <div className='about-header flex flex-col text-center'>
                    <h2 className='text-white text-2xl capitalize'>Our mission is to make high-quality sound accessible to everyone.</h2>
                    <p className='text-white font-thin text-xl mt-5'>Your ears deserve better. </p>
                </div>
            </div>
        </div>
        <div className='lg:grid xl:grid grid-cols-2 lg:gap-3 items-center align-middle px-10 py-10 xs:p-12'>
            <img src='/assets/newimg/jonas-schindler-6LgGeKPWpSA-unsplash.jpg' className='w-85 hidden lg:flex xl:flex' data-aos="fade-right" data-aos-once="true" />
            <div className='text-white flex flex-col items-center gap-6' data-aos="fade-left" data-aos-once="true">
                <h2 className='text-xl uppercase text-center lg:text-3xl xl:text-4xl'>Experience sound like never before.</h2>
                <p className='text-md capitalize text-center lg:text-lg xl:text-xl'>
                    We focus on quality, performance, and customer satisfaction.
                </p>
                <p className='capitalize text-center text-md lg:text-lg xl:text-xl'>
                    Every product we sell is tested to ensure crystal-clear audio and lasting comfort.
                </p>
            </div>
        </div>
        <div className="underline-content"></div>
        <div className='lg:grid xl:grid grid-cols-2 items-center py-10 px-10 gap-x-16 xs:p-12'>
            <div className='text-white flex flex-col items-center gap-6' data-aos="fade-right" data-aos-once="true">
                <h2 className='text-xl uppercase text-center lg:text-3xl xl:text-4xl'>The future of audio, delivered today</h2>
                <p className='text-md capitalize text-center lg:text-lg xl:text-xl'>
                    Whether you're working, gaming, or relaxing, we believe your earbuds should match your lifestyle.
                </p>
            </div>
            <img src='/assets/newimg/michael-marais-qQu4gTORkys-unsplash.jpg' className='w-9/12 hidden lg:flex xl:flex' data-aos="fade-left" data-aos-once="true"/>
        </div>
        <div className="underline-content"></div>
        <div className='lg:grid xl:grid grid-cols-2 items-center px-10 py-10 gap-x-16 xs:p-12'>
            <img src='/assets/newimg/shawnn-tan-eNWN3dEY6bY-unsplash.jpg' className='hidden lg:flex xl:flex' data-aos="fade-right" data-aos-once="true" />
            <div className='text-white flex flex-col items-center gap-6' data-aos="fade-left" data-aos-once="true">
                <h2 className='text-xl uppercase lg:text-3xl xl:text-4xl'>24/7 support team ready to help</h2>
                <p className='text-md capitalize text-center lg:text-lg xl:text-xl'>
                    Every product we sell is tested to ensure crystal-clear audio and lasting comfort.
                </p>
            </div>
        </div>
        <div className='about-us px-10 py-24'>
            <div className='about-us-content text-white flex flex-col items-center text-center gap-6 ' data-aos="fade-up" data-aos-once="true">
                <h2 className='text-3xl uppercase'>who are we?</h2>
                <p className='text-xl capitalize'>At Hearly, we believe everyone deserves the best audio experience, no matter the budget.</p>
                <p className='text-xl capitalize'>We started with a simple idea: make premium wireless earbuds accessible and enjoyable for all.</p>
            </div>
        </div>
    </section>
  )
}

export default About
