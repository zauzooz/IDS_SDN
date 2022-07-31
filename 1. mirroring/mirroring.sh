ovs-vsctl del-port sw1-eth1;
ovs-vsctl add-port sw1 sw1-eth1 -- --id=@p get port sw1-eth1 -- --id=@m create mirror name=m0 select-all=true output-port=@p -- set bridge sw1 mirrors=@m;
