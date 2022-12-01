import './App.css';

function App() {
  return (
    <div className="App">
      <div className="Layout">
        <div className="Left">
          <h2>Star Map</h2>
          <div className='Box'>

          </div>
        </div>
        <div className="Right">
          <div className='Right-Top'>
            <h3>Location: <i>Los Angeles</i></h3>
            <h3>Time: <i>6:40</i></h3>
          </div>
          <div className="List">
            <div className='List-Option'>
              <div className='List-Left'>
                <h3>Star Name: Sirius</h3>
              </div>
              <div className='List-Right'>
                <div className='Star-Image'/>
              </div>
            </div>

            <div className='List-Option'>
              <div className='List-Left'>
                <h3>Star Name: Canopus</h3>
              </div>
              <div className='List-Right'>
                <div className='Star-Image'/>
              </div>
            </div>

            <div className='List-Option'>
              <div className='List-Left'>
                <h3>Star Name: Rigil Kentaurus</h3>
              </div>
              <div className='List-Right'>
                <div className='Star-Image'/>
              </div>
            </div>

            <div className='List-Option'>
              <div className='List-Left'>
                <h3>Star Name: Arcturus</h3>
              </div>
              <div className='List-Right'>
                <div className='Star-Image'/>
              </div>
            </div>

            <div className='List-Option'>
              <div className='List-Left'>
                <h3>Star Name: Vega</h3>
              </div>
              <div className='List-Right'>
                <div className='Star-Image'/>
              </div>
            </div>

            <div className='List-Option'>
              <div className='List-Left'>
                <h3>Star Name: Capella</h3>
              </div>
              <div className='List-Right'>
                <div className='Star-Image'/>
              </div>
            </div>
          </div>
          <div className='Button'>
            <h3>Search for Star</h3>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
